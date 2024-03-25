from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship,backref

from schema.request import CreateMenuRequest, CreateOrdersRequest

Base = declarative_base()



class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    price = Column(Integer)
    temperature = Column(Boolean, nullable=False)

    @classmethod
    def create(cls, request: CreateMenuRequest) -> "Menu":
        return cls(
            id = request.id,
            name = request.name,
            price = request.price,
            temperature = request.temperature,
        )
    # order_id = Column(Integer, ForeignKey('orders.id'))  # order 테이블과의 관계 설정
    # # order 객체에 대한 back reference 설정
    # orders = relationship("Orders", back_populates="menu")

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    menu_id = Column(Integer, ForeignKey('menu.id'))  # menu 테이블의 id를 참조하는 외래 키
    menu = relationship("Menu")  # Menu 클래스와의 관계 설정

    @classmethod
    def create(cls, request: CreateOrdersRequest) -> "Orders":
        return cls(
            menu_id = request.menu_id
        )

