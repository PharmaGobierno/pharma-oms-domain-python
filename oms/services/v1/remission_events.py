from typing import Iterator, List, Optional, Tuple

from oms.models.v1.remission_events import RemissionEventsModel
from oms.repository_interfaces.v1.remission_events import RemissionEventsRepository

from ._base import BaseService


class RemissionEventsService(
    BaseService[RemissionEventsModel, RemissionEventsRepository]
):
    __model__ = RemissionEventsModel

    def get_by_tracking_id(
        self,
        tracking_id: str,
        *,
        tenant: Optional[List[str]] = None,
        sort: Optional[List[Tuple[str, int]]] = None,
        limit: Optional[int] = None
    ) -> Tuple[int, Iterator[RemissionEventsModel]]:
        count, result = self.repository.get_by_tracking_id(
            tracking_id, tenant=tenant, sort=sort, limit=limit
        )
        return count, map(lambda r: RemissionEventsModel(**r), result)
