from oms.models.v1.remission_events import RemissionEventsModel
from oms.repository_interfaces.v1.remission_events import (
    RemissionEventsRepositoryInterface,
)

from ._base import BaseService


class RemissionEventsService(
    BaseService[RemissionEventsModel, RemissionEventsRepositoryInterface]
):
    __model__ = RemissionEventsModel
