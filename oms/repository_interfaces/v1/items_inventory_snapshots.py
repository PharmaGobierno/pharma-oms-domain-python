from abc import abstractmethod
from typing import Iterator, List, Optional, Tuple, Union

from ._base import BaseRepository


class ItemsInventorySnapshotsRepository(BaseRepository):
    @abstractmethod
    def get_by_item_sku(
        self,
        sku: str,
        *,
        quantity_gte: Optional[int] = None,
        sort: Optional[List[Tuple[str, int]]] = None,
        projection: Optional[Union[list, dict]] = None,
        limit: Optional[int] = None,
    ) -> Tuple[int, Iterator[dict]]:
        raise NotImplementedError
