from oms.models.v1.remission_changelogs import RemissionChangelogsModel
from oms.repository_interfaces.v1.remission_changelogs import (
    RemissionChangelogsRepositoryInterface,
)

from ._base import BaseService


class RemissionChangelogsService(
    BaseService[RemissionChangelogsModel, RemissionChangelogsRepositoryInterface]
):
    __model__ = RemissionChangelogsModel
