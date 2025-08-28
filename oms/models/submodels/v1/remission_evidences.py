from dataclasses import dataclass
from typing import Literal, Optional

from ._enums import EvidenceType

@dataclass
class RemissionEvidence:
    value: str
    version: Literal["1.0.0"] = "1.0.0"
    type: Optional[EvidenceType] = None
    validation_timestamp: Optional[int] = None
    validation_status: Optional[str] = None  # TODO: Define enum
