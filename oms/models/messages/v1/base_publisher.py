from dataclasses import asdict, dataclass, field
from time import time
from typing import Any, Dict, Optional

from oms.models.submodels.v1.tenant import Tenant
from oms.models.v1.minified.users import UsersMin


@dataclass
class BasePubsubMessage:
    payload: Any
    origin_timestamp: int
    author: UsersMin
    version: str
    tenant: Optional[str] = None
    published_at: int = field(default_factory=lambda: round(time() * 1000))
    context: Optional[dict] = None

    def dict(self):
        return asdict(self)

    @classmethod
    def topic(cls) -> str:
        raise NotImplementedError

    def get_attributes(self) -> Dict[str, str]:
        default_attrs = {"topic": self.topic(), "version": self.version}
        if self.tenant:
            tenant = Tenant.decode(tenant=self.tenant)
            default_attrs.update({"company": tenant.company, "project": tenant.project})
        return default_attrs


@dataclass
class BaseKafkaMessage:
    payload: Any
    origin_timestamp: int
    author: UsersMin
    version: str
    published_at: int = field(default_factory=lambda: round(time() * 1000))
    context: Optional[dict] = None

    def dict(self):
        return asdict(self)

    def topic(self) -> str:
        raise NotImplementedError

    def get_headers(self) -> Dict[str, str]:
        return {"topic": self.topic(), "version": self.version}
