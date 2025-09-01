from dataclasses import dataclass
from typing import Literal, Optional

from ._enums import EvidenceType


@dataclass
class RemissionEvidence:
    value: str
    file_type: EvidenceType
    origin_timestamp: Optional[int] = None
    document_name: Optional[str] = None  # TODO: Define enum
    version: Literal["1.0.0"] = "1.0.0"
