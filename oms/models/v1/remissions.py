from dataclasses import dataclass
from typing import List, Optional

from oms.models.submodels.v1.remission_destinations import RemissionDestination
from oms.models.v1.minified.users import UsersMin

from ._base import UpdatableModel, uuid_by_params
from ._enums import OrderTypes, RemissionEvents


@dataclass(kw_only=True)
class RemissionsModel(UpdatableModel):
    __entity_name__ = "remissions"

    tracking_id: str
    order_number: str
    foreign_id: Optional[str] = None
    order_type: OrderTypes
    items: List[str]  # list[skus]
    delivery_destination: RemissionDestination
    delivery_date: int
    delivery_id: Optional[str] = None
    appointment_develery_date: Optional[int] = None
    current_event: Optional[RemissionEvents] = None
    current_event_timestamp: Optional[int] = None
    author: Optional[UsersMin] = None
    institution: Optional[dict] = None  # {id:str, name:str} ?

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.tracking_id)
