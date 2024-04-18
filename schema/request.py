from pydantic import BaseModel, ConfigDict


class MenuRequest(BaseModel):
    id : int
    name : str
    price : int
    temperature : bool

class CreateMenuRequest(BaseModel):
    id: int
    name: str
    price: int
    temperature: bool

class CreateOrdersRequest(BaseModel):
    menu_id : int






