from dataclasses import dataclass

from oms.models.v1.minified.users import UsersMin

from ._base import BaseModel, uuid_by_params
from ._enums import OrderTypes


@dataclass(kw_only=True)
class RemissionIntegrationRequestLogsModel(BaseModel):
    __entity_name__ = "remission-integration-request-logs"
    order_number: str
    order_type: OrderTypes
    payload: dict
    origin_platform: str
    origin_timestamp: int
    author: UsersMin

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.order_number, self.origin_timestamp)
