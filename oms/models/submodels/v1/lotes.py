from dataclasses import dataclass
from typing import Literal


@dataclass
class Lote:
    sku: str
    lote: str
    expiration_date: int
    accepted_quantity: int

    version: Literal["1.0.0"] = "1.0.0"
