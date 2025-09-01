from oms.models.v1.remission_integration_request_logs import (
    RemissionIntegrationRequestLogsModel,
)
from oms.repository_interfaces.v1.remission_integration_request_logs import (
    RemissionIntegrationRequestLogsRepository,
)

from ._base import BaseService


class RemissionChangelogsService(
    BaseService[
        RemissionIntegrationRequestLogsModel, RemissionIntegrationRequestLogsRepository
    ]
):
    __model__ = RemissionIntegrationRequestLogsModel
