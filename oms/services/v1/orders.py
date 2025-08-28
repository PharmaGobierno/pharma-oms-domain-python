from oms.models.v1.orders import OrdersModel
from oms.repository_interfaces.v1.orders import OrdersRepositoryInterface

from ._base import BaseService


class OrdersService(BaseService[OrdersModel, OrdersRepositoryInterface]):
    __model__ = OrdersModel
