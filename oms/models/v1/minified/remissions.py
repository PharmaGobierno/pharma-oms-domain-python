from dataclasses import dataclass
from typing import Optional


@dataclass
class RemissionsMin:
    id: str
    tenant_id: str
    tracking_id: str
    order_number: str
    order_type: str
    delivery_date: int
    delivery_destination_id: Optional[str] = None
    tracking_wapper_id: Optional[str] = None  # wrapper for trackings
