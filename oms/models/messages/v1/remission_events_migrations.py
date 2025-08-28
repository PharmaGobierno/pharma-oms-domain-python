from dataclasses import dataclass
from typing import Dict

from ._enums import RemissionMigrationOrigins
from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class RemissionEventMigrationsPubsubMessage(BasePubsubMessage):
    payload: dict
    tracking_id: str
    remission_id: str
    migration_log_id: str
    event: str
    event_timestamp: int
    event_signature: str
    origin: RemissionMigrationOrigins
    origin_id: str
    version: str = "1"

    def __post_init__(self):
        self.event_signature = self.event + str(self.event_timestamp) + self.origin_id

    @classmethod
    def topic(cls) -> str:
        return "oms-remission-events-migrations"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {
            **default_attributes,
            "origin": self.origin.value,
            "origin_id": self.origin_id,
        }
