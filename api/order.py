from typing import List

from fastapi import APIRouter, Depends, HTTPException

from database.orm import Orders
from database.repository import OrdersRepository
from schema.request import CreateOrdersRequest
from schema.resopnse import OrdersSChema, MenuListSchema, MenuSchema

router = APIRouter(prefix="/users")

@router.post("/orders",status_code=201)
def create_orders(
        request: CreateOrdersRequest,
        order_repo: OrdersRepository = Depends()
) -> OrdersSChema:
    orders : Orders = Orders.create(request = request)
    orders: Orders = order_repo.create_order(orders = orders)
    return OrdersSChema.from_orm(orders)

@router.get("/orders/{orders_id}",status_code=200)
def get_orders(
    orders_id : int ,
    order_repo: OrdersRepository = Depends()
)-> MenuSchema:
    orders: Orders | None = order_repo.get_order_by_order_id(orders_id)
    menus: List[orders] = orders.menu
    return MenuSchema.from_orm(menus)

