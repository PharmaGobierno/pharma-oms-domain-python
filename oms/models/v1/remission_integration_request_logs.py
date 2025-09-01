from dataclasses import dataclass

from oms.models.v1.minified.users import UsersMin

from ._base import BaseModel


@dataclass(kw_only=True)
class RemissionIntegrationRequestLogsModel(BaseModel):
    __entity_name__ = "remission-integration-request-logs"
    order_number: str
    payload: dict
    origin_platform: str
    origin_timestamp: int
    author: UsersMin
