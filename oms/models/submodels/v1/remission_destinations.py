from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class RemissionDestination:
    id: str
    version: Literal["1.0.0"] = "1.0.0"
    name: Optional[str] = None
    company: Optional[str] = None
