from dataclasses import dataclass
from typing import Dict

from oms.models.v1.remission_events import RemissionEventsModel

from ._enums import EntityActionTypes
from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class RemissionEventsPubsubMessage(BasePubsubMessage):
    payload: RemissionEventsModel
    event: str
    action_type: EntityActionTypes
    origin_platform: str
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "oms-remission-events"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {
            **default_attributes,
            "event": self.event,
            "action_type": self.action_type.value,
            "origin_platform": self.origin_platform,
        }
