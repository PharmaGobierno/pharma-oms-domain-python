from dataclasses import dataclass
from typing import Dict

from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class RemissionIntegrationsPubsubMessage(BasePubsubMessage):
    payload: dict
    origin_platform: str
    order_type: str
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "pharma-oms-remission-integrations"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {
            **default_attributes,
            "order_type": self.order_type,
            "origin_platform": self.origin_platform,
        }
