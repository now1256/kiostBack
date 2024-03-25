from fastapi import FastAPI

from api import user
from api import order
app = FastAPI()

app.include_router(user.router)
app.include_router(order.router)
