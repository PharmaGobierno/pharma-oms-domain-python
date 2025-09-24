from dataclasses import dataclass
from typing import List, Optional

from oms.models.submodels.v1.remission_destinations import RemissionDestination
from oms.models.v1.minified.users import UsersMin

from ._base import MinifiableModel, UpdatableModel, uuid_by_params
from .minified.remissions import RemissionsMin


@dataclass(kw_only=True)
class RemissionsModel(UpdatableModel, MinifiableModel[RemissionsMin]):
    __entity_name__ = "remissions"

    tracking_id: str
    order_number: str
    tracking_wapper_id: Optional[str] = None  # wrapper for trackings
    foreign_id: Optional[str] = None
    order_type: str
    items: List[str]  # list[skus]
    delivery_destination: RemissionDestination
    delivery_date: int
    author: UsersMin
    oms_entity_type: Optional[str] = None
    delivery_id: Optional[str] = None
    appointment_delivery_date: Optional[int] = None
    current_event: Optional[str] = None
    current_event_timestamp: Optional[int] = None
    institution_number: Optional[str] = None
    metadata: Optional[dict] = None  # free-form json

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.tracking_id)

    def minified(self) -> RemissionsMin:
        return RemissionsMin(
            id=self._id,
            tenant_id=self.tenant_id,
            tracking_id=self.tracking_id,
            order_number=self.order_number,
            order_type=self.order_type,
            delivery_date=self.delivery_date,
            delivery_destination_id=self.delivery_destination.id,
            tracking_wapper_id=self.tracking_wapper_id,
        )
