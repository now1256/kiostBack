from pydantic import BaseModel

class MenuSchema(BaseModel):
    id: int
    name: str
    price: int
    temperature: bool


    class Config:
        # pydantic version change orm_mode -> from_attributes
        from_attributes = True