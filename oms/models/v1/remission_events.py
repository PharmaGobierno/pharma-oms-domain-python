from dataclasses import dataclass, field
from typing import List, Optional

from oms.models.submodels.v1.remission_event_notes import RemissionEventNote
from oms.models.submodels.v1.remission_evidences import RemissionEvidence
from oms.models.v1.minified.users import UserMin

from ._base import EventfulModel, uuid_by_params
from ._enums import RemissionEvents, RemissionEventWarnings


@dataclass(kw_only=True)
class RemissionEventsModel(EventfulModel[RemissionEvents]):
    __entity_name__ = "remission-events"

    remission_id: str
    tracking_id: str
    author: UserMin
    evidences: Optional[List[RemissionEvidence]] = None
    load_id: Optional[str] = None
    loaded_amount: Optional[int] = None
    delivered_amount: Optional[int] = None
    metadata: Optional[dict] = None
    event_note: RemissionEventNote = field(default_factory=RemissionEventNote)
    warnings: Optional[List[RemissionEventWarnings]] = None
    origin_platform: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.tracking_id, self.event_timestamp)
