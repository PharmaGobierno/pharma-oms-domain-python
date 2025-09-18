from typing import Iterator, List, Optional, Tuple

from oms.models.v1.items_inventory_snapshots import ItemsInventorySnapshotsModel
from oms.repository_interfaces.v1.items_inventory_snapshots import (
    ItemsInventorySnapshotsRepository,
)

from ._base import BaseService


class ItemsInventorySnapshotsService(
    BaseService[ItemsInventorySnapshotsModel, ItemsInventorySnapshotsRepository]
):
    __model__ = ItemsInventorySnapshotsModel

    def get_by_item_sku(
        self,
        sku: str,
        *,
        quantity_gte: Optional[int] = None,
        origin_warehouse: Optional[str] = None,
        company: Optional[str] = None,
        project: Optional[str] = None,
        sort: Optional[List[Tuple[str, int]]] = None,
        limit: Optional[int] = None
    ) -> Tuple[int, Iterator[ItemsInventorySnapshotsModel]]:
        count, result = self.repository.get_by_item_sku(
            sku,
            quantity_gte=quantity_gte,
            origin_warehouse=origin_warehouse,
            company=company,
            project=project,
            sort=sort,
            limit=limit,
        )
        return count, map(lambda r: ItemsInventorySnapshotsModel(**r), result)
