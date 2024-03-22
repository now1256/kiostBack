from pydantic import BaseModel, ConfigDict


class MenuRequest(BaseModel):
    id : int
    name : str
    price : int
    temperature : bool


