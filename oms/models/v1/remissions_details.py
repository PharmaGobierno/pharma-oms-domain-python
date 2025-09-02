from dataclasses import dataclass
from typing import List, Optional

from oms.models.submodels.v1.items import Item
from oms.models.submodels.v1.lotes import Lote
from oms.models.v1.minified.remissions import RemissionsMin
from oms.models.v1.minified.users import UsersMin

from ._base import UpdatableModel, uuid_by_params


@dataclass(kw_only=True)
class RemissionDetailsModel(UpdatableModel):
    __entity_name__ = "remission-details"

    remission: RemissionsMin
    item: Item
    lotes: List[Lote]
    author: Optional[UsersMin] = None

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.remission.id, self.item.id)
