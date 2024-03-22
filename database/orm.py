from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship,backref

Base = declarative_base()


# class Client(Base):
#     __tablename__ = 'client'
#
#     id = Column(Integer, primary_key=True)

class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    price = Column(Integer)
    temperature = Column(Boolean, nullable=False)

    # order_id = Column(Integer, ForeignKey('orders.id'))  # order 테이블과의 관계 설정
    # # order 객체에 대한 back reference 설정
    # orders = relationship("Orders", back_populates="menu")

# class Orders(Base):
#     __tablename__ = 'orders'
#     id = Column(Integer, primary_key=True)
#     client_id = Column(Integer, ForeignKey('client.id'))  # client 테이블과의 관계 설정
#     # client 객체에 대한 back reference 설정
#     client = relationship("Client", back_populates="orders")
#     # menu 객체에 대한 back reference 설정
#     menu = relationship("Menu", back_populates="orders")


