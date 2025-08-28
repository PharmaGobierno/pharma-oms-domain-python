from oms.models.v1.remission_events_migration_logs import \
    RemissionEventsMigrationLogsModel
from oms.repository_interfaces.v1.remission_events_migration_logs import \
    RemissionEventsMigrationLogsRepositoryInterface

from ._base import BaseService


class RemissionEventsMigrationLogsService(
    BaseService[RemissionEventsMigrationLogsModel, RemissionEventsMigrationLogsRepositoryInterface]
):
    __model__ = RemissionEventsMigrationLogsModel
