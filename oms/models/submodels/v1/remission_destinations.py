from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class RemissionDestination:
    id: str
    displayable_name: str = ""
    company: Optional[str] = None
    version: Literal["1.0.0"] = "1.0.0"
