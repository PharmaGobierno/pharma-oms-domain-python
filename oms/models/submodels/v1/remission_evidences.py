from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class RemissionEvidence:
    value: str
    file_type: str
    origin_timestamp: Optional[int] = None
    document_name: Optional[str] = None

    version: Literal["1.0.0"] = "1.0.0"
