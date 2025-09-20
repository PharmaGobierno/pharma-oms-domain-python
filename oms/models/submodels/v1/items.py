from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class Item:
    id: str
    sku: str
    brand: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[int] = None

    version: Literal["1.0.0"] = "1.0.0"
