from abc import ABC, abstractmethod
from base64 import urlsafe_b64encode
from dataclasses import asdict, dataclass, field, fields, is_dataclass
from enum import Enum
from time import time
from typing import Generic, TypeVar
from uuid import NAMESPACE_OID, UUID, uuid4, uuid5

EventAttributeT = TypeVar("EventAttributeT", bound="Enum")
MinifiedObjectT = TypeVar("MinifiedObjectT")


def uuid_by_params(*args):
    """Generates a UUIDv5 based on the given parameters.

    Args:
        *args: Variable number of arguments used to create the UUID.

    Returns:
        str: The generated UUID as a string.
    """
    value = "#".join(map(str, args))
    return str(uuid5(namespace=NAMESPACE_OID, name=value))


def short_uuid(*args) -> str:
    """Generates a short, URL-safe UUID based on the given parameters."""
    long_uuid = UUID(uuid_by_params(*args))
    return urlsafe_b64encode(long_uuid.bytes).rstrip(b"=").decode()


@dataclass
class BaseModel:
    tenant_id: str
    _id: str = field(default_factory=lambda: str(uuid4()))
    created_at: int = field(default_factory=lambda: round(time() * 1000))
    version: str = "1.0.0"

    @classmethod
    def get_entity_name(cls) -> str:
        if not getattr(cls, "__entity_name__", None):
            raise TypeError(
                f"__entity_name__ must be defined at " f"{cls.__class__.__name__} model"
            )
        return str(getattr(cls, "__entity_name__", None))

    def dict(self):
        return asdict(self)

    @classmethod
    def _dict_to_dataclasses(cls, instance):
        """Convert all fields of type `dataclass` into an instance of the
        specified data class if the current value is of type dict."""
        for f in fields(cls):
            if not is_dataclass(f.type):
                continue

            value = getattr(instance, f.name)
            if not isinstance(value, dict):
                continue

            new_value = f.type(**value)  # type: ignore
            setattr(instance, f.name, new_value)

    def __post_init__(self):
        self._dict_to_dataclasses(self)


@dataclass(kw_only=True)
class UpdatableModel(BaseModel):
    updated_at: int = field(default_factory=lambda: round(time() * 1000))

    def update(self, data: dict):
        """Update the model with the given data."""
        data.update({"updated_at": round(time() * 1000)})
        valid_fields = {f.name for f in fields(self)}
        for key, value in data.items():
            if key in valid_fields:
                setattr(self, key, value)
        self._dict_to_dataclasses(self)


@dataclass(kw_only=True)
class EventfulModel(BaseModel):
    """A generic dataclass representing a event entity with
    event timestamp. Using in event sourcing entities

    Attributes:
        event_timestamp (int): The timestamp of the event
            event.
        event (EventAttributeT): The current event of the entity.
    """

    event_timestamp: int
    event: str


@dataclass(kw_only=True)
class MinifiableModel(Generic[MinifiedObjectT], ABC):
    @abstractmethod
    def minified(self) -> MinifiedObjectT:
        raise NotImplementedError
