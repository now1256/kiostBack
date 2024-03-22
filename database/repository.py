from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.connection import get_db
from database.orm import Menu

class MenuRepository:
    def __init__(self, session:Session = Depends(get_db)):
        self.session = session

    def get_Menu(self) -> Menu | None:
        return self.session.scalar(select(Menu))

    # def get_todo_by_todo_id(self, todo_id: int) -> ToDo | None:
    #     return self.session.scalar(select(ToDo).where(ToDo.id == todo_id))
    #
    # # 생성한 orm 객체를 self 오브젝트에 추가
    # # 쌓인 데이터를 commit으로 저장
    # # id를 저장 기본키 refresh를 통해 db에서 읽어옴
    # def create_todo(self, todo: ToDo) -> ToDo:
    #     self.session.add(instance= todo)
    #     self.session.commit()
    #     self.session.refresh(instance= todo)
    #     return todo
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