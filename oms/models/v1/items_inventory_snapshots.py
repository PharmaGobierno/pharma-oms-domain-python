from dataclasses import dataclass
from typing import Optional

from ._base import UpdatableModel, uuid_by_params


@dataclass(kw_only=True)
class ItemsInventorySnapshotsModel(UpdatableModel):
    __entity_name__ = "items-inventory-snapshots"

    item_id: str
    item_sku: str
    lote_id: str
    lote_expiration_date: int
    lote_quantity: int
    origin_warehouse: str
    origin_timestamp: int
    item_description: Optional[str] = None
    item_brand: Optional[str] = None
    project: str
    company: str
    origin_platform: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(
            self.item_id,
            self.lote_id,
            self.project,
            self.company,
        )
