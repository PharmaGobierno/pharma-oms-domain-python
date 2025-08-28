from dataclasses import dataclass

from oms.models.v1.minified.users import UserMin

from ._base import BaseModel


@dataclass(kw_only=True)
class RemissionChangelogsModel(BaseModel):
    __entity_name__ = "remission-changelogs"
    tracking_id: str
    payload: dict
    action_type: str
    origin_platform: str
    origin_timestamp: int
    author: UserMin
