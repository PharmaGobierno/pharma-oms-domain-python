from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class RemissionEventNote:
    version: Literal["1.0.0"] = "1.0.0"
    type: Optional[str] = None
    comment: Optional[str] = None
    motive_rejection: Optional[str] = None
    submotive_rejection: Optional[str] = None
