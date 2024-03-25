from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.connection import get_db
from database.orm import Menu, Orders


class MenuRepository:
    def __init__(self, session:Session = Depends(get_db)):
        self.session = session

    def get_menus(self) -> List[Menu] :
        return self.session.execute(select(Menu)).scalars().all()

    def get_menu_by_menu_id(self, menu_name: str) -> Menu | None:
        return self.session.scalar(select(Menu).where(Menu.name == menu_name))

    # id를 저장 기본키 refresh를 통해 db에서 읽어옴
    def create_menu(self, menu: Menu) -> Menu:
        self.session.add(instance= menu)
        self.session.commit()
        self.session.refresh(instance= menu)
        return menu
    #
    # def update_todo(self, todo: ToDo) -> ToDo:
    #     self.session.add(instance=todo)
    #     self.session.commit()
    #     self.session.refresh(instance=todo)
    #     return todo
    #
    # def delete_todo(self, todo_id :int) -> None:
    #     self.session.execute(delete(ToDo).where(ToDo.id == todo_id))
    #     self.session.commit()

class OrdersRepository:
    def __init__(self, session:Session = Depends(get_db)):
        self.session = session
    def get_order_by_order_id(self, order_id: int) -> Orders | None:
        return self.session.scalar(select(Orders).where(Orders.id == order_id))

    def create_order(self, orders: Orders) -> Orders:
        self.session.add(instance= orders)
        self.session.commit()
        self.session.refresh(instance= orders)
        return orders