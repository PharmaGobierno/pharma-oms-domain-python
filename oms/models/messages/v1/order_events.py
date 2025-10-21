from dataclasses import dataclass
from typing import Dict, Optional

from ._enums import EntityActionTypes
from .base_publisher import BasePubsubMessage, Tenant


@dataclass(kw_only=True)
class OrderEventsPubsubMessage(BasePubsubMessage):
    payload: dict
    event: str
    action_type: EntityActionTypes
    oms_entity_type: str
    origin_platform: str
    version: str = "1"
    project: Optional[str] = None
    company: Optional[str] = None

    @classmethod
    def topic(cls) -> str:
        return "oms.order_events"

    def __post_init__(self):
        if self.tenant:
            tenant = Tenant.decode(tenant=self.tenant)
            self.company = tenant.company
            self.project = tenant.project

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {
            **default_attributes,
            "event": self.event,
            "action_type": self.action_type.value,
            "oms_entity_type": self.oms_entity_type,
            "origin_platform": self.origin_platform,
        }
