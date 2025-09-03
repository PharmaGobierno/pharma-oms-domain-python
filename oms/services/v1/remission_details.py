from typing import Iterator, List, Optional, Tuple

from oms.models.v1.remissions_details import RemissionDetailsModel
from oms.repository_interfaces.v1.remission_details import RemissionDetailsRepository

from ._base import BaseService


class RemissionDetailsService(
    BaseService[RemissionDetailsModel, RemissionDetailsRepository]
):
    __model__ = RemissionDetailsModel

    def get_by_tracking_id(
        self,
        tracking_id: str,
        *,
        tenant: Optional[List[str]] = None,
        sort: Optional[List[Tuple[str, int]]] = None,
        limit: Optional[int] = None
    ) -> Tuple[int, Iterator[RemissionDetailsModel]]:
        count, result = self.repository.get_by_tracking_id(
            tracking_id, tenant=tenant, sort=sort, limit=limit
        )
        return count, map(lambda r: RemissionDetailsModel(**r), result)
