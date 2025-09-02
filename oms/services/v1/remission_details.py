from oms.models.v1.remissions_details import RemissionDetailsModel
from oms.repository_interfaces.v1.remission_details import RemissionDetailsRepository

from ._base import BaseService


class RemissionDetailsService(
    BaseService[RemissionDetailsModel, RemissionDetailsRepository]
):
    __model__ = RemissionDetailsModel
