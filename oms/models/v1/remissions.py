from dataclasses import dataclass
from typing import Optional

from oms.models.submodels.v1.remission_destinations import RemissionDestination
from oms.models.v1.minified.items import ItemMin
from oms.models.v1.minified.users import UserMin

from ._base import UpdatableModel, uuid_by_params
from ._enums import RemissionEvents


@dataclass(kw_only=True)
class RemissionsModel(UpdatableModel):
    __entity_name__ = "remissions"

    tracking_id: str
    order_id: str
    current_event: Optional[RemissionEvents] = None
    current_event_timestamp: Optional[int] = None
    last_load: Optional[str] = None
    last_author: Optional[UserMin] = None
    original_amount: Optional[int] = None
    item: Optional[ItemMin] = None
    lote: Optional[str] = None
    destination: Optional[RemissionDestination] = None
    order_supply: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.tracking_id)
