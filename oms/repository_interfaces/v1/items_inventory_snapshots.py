from abc import abstractmethod
from typing import Iterator, List, Optional, Tuple

from ._base import BaseRepository


class ItemsInventorySnapshotsRepository(BaseRepository):
    @abstractmethod
    def get_by_item_sku(
        self,
        sku: str,
        *,
        quantity_gte: Optional[int] = None,
        company: Optional[str] = None,
        project: Optional[str] = None,
        sort: Optional[List[Tuple[str, int]]] = None,
        limit: Optional[int] = None,
    ) -> Tuple[int, Iterator[dict]]:
        raise NotImplementedError
