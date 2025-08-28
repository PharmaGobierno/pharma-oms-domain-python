from dataclasses import dataclass
from typing import List

from ._base import UpdatableModel, uuid_by_params
from ._enums import OrderTypes


@dataclass(kw_only=True)
class OrdersModel(UpdatableModel):
    __entity_name__ = "orders"

    tracking_id: str
    current_type: OrderTypes
    types: List[OrderTypes]

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.tracking_id, self.current_type)
