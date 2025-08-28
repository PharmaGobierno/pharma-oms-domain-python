from dataclasses import dataclass, field
from typing import List, Optional

from ._base import BaseModel, uuid_by_params
from ._enums import RemissionMigrationOrigins


@dataclass(kw_only=True)
class RemissionEventsMigrationLogsModel(BaseModel):
    __entity_name__ = "remission-events-migration-logs"

    tracking_id: str
    origin_type: RemissionMigrationOrigins
    origin_id: Optional[str] = None
    origin_timestamp: int
    processed_events: List[str] = field(default_factory=list)
    migration_payload: dict

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.origin_timestamp, self.origin_id)
