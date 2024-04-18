from fastapi import FastAPI

from api import menu
from api import order
from api import LLM

# initialize db tables
# TODO migrate to alembic
# models.Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(menu.router)
app.include_router(order.router)
app.include_router(LLM.router)