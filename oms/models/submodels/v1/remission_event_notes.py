from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class RemissionEventNote:
    comment: str
    subcomment: Optional[str] = None
    note_type: Optional[str] = None
    version: Literal["1.0.0"] = "1.0.0"
