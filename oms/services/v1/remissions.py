from typing import Iterator, List, Optional, Tuple

from oms.models.v1.remissions import RemissionsModel
from oms.repository_interfaces.v1.remissions import RemissionsRepository

from ._base import BaseService


class RemissionsService(BaseService[RemissionsModel, RemissionsRepository]):
    __model__ = RemissionsModel

    def get_by_tracking_id(
        self,
        tracking_id: str,
        *,
        tenant: Optional[List[str]] = None,
    ) -> Tuple[int, Iterator[RemissionsModel]]:
        count, result = self.repository.get_by_tracking_id(tracking_id, tenant=tenant)
        return count, map(lambda r: RemissionsModel(**r), result)

    def search_by_tracking(
        self,
        search_str: str,
        *,
        page: int,
        limit: int,
        created_at_gt: Optional[int] = None,
        created_at_lt: Optional[int] = None,
        tenant: Optional[List[str]] = None,
        events: Optional[List[str]] = None,
    ) -> Tuple[int, Iterator[RemissionsModel]]:
        count, result = self.repository.search_by_tracking(
            search_str,
            page=page,
            limit=limit,
            created_at_gt=created_at_gt,
            created_at_lt=created_at_lt,
            tenant=tenant,
            events=events,
        )
        return count, map(lambda r: RemissionsModel(**r), result)
