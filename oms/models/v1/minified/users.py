from dataclasses import dataclass
from typing import Optional


@dataclass
class UsersMin:
    id: str
    name: str
    type: Optional[str] = None
    email: Optional[str] = None
