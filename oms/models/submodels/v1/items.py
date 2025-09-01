from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class ItemMin:
    id: str
    sku: str
    description: Optional[str] = None
    quantity: Optional[int] = None
    version: Literal["1.0.0"] = "1.0.0"
