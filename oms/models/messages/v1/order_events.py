from dataclasses import dataclass
from typing import Dict

from ._enums import EntityActionTypes
from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class OrderEventsPubsubMessage(BasePubsubMessage):
    payload: dict
    event: str
    action_type: EntityActionTypes
    oms_entity_type: str
    origin_platform: str
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "oms.order_events"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {
            **default_attributes,
            "event": self.event,
            "action_type": self.action_type.value,
            "oms_entity_type": self.oms_entity_type,
            "origin_platform": self.origin_platform,
        }
