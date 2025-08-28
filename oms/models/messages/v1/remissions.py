from dataclasses import dataclass
from typing import Dict

from oms.models.v1.remissions import RemissionsModel

from ._enums import EntityActionTypes
from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class RemissionsPubsubMessage(BasePubsubMessage):
    payload: RemissionsModel
    origin_platform: str
    action_type: EntityActionTypes
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "oms-remissions"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {
            **default_attributes,
            "action_type": self.action_type.value,
        }
