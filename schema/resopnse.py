from typing import List

from pydantic import BaseModel

class MenuSchema(BaseModel):
    id: int
    name: str
    price: int
    temperature: bool
    class Config:
        # pydantic version change orm_mode -> from_attributes
        from_attributes = True
class MenuListSchema(BaseModel):
    menus: List[MenuSchema]

    class Config:
        # pydantic version change orm_mode -> from_attributes
        from_attributes = True

class OrdersSChema(BaseModel):
    id : int
    menu_id: int
    class Config:
        # pydantic version change orm_mode -> from_attributes
        from_attributes = True