from dataclasses import dataclass
from typing import Literal


@dataclass
class RemissionDestination:
    id: str
    customer: str
    version: Literal["1.0.0"] = "1.0.0"
