from dataclasses import dataclass
from typing import List, Optional

from oms.models.submodels.v1.remission_event_notes import RemissionEventNote
from oms.models.submodels.v1.remission_evidences import RemissionEvidence
from oms.models.v1.minified.remissions import RemissionsMin
from oms.models.v1.minified.users import UsersMin

from ._base import EventfulModel, UpdatableModel, uuid_by_params


@dataclass(kw_only=True)
class RemissionEventsModel(
    UpdatableModel,
    EventfulModel,
):
    __entity_name__ = "remission-events"

    remission: RemissionsMin
    author: UsersMin
    evidences: Optional[List[RemissionEvidence]] = None
    metadata: Optional[dict] = None
    event_note: Optional[RemissionEventNote] = None
    warnings: Optional[List[str]] = None
    origin_platform: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.remission.tracking_id, self.event_timestamp)
