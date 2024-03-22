from fastapi import APIRouter, Depends, HTTPException

from database.orm import Menu
from database.repository import MenuRepository
from schema.request import MenuRequest
from schema.resopnse import MenuSchema

router = APIRouter(prefix="/users")

@router.get("/menus",status_code=201)
def get_menu_handler(
        menu_repo: MenuRepository = Depends()
) -> MenuSchema:
    menu: Menu | None = menu_repo.get_Menu()
    if menu:
        return MenuSchema.from_orm(menu)
    raise HTTPException(status_code=404, detail="menu Not Found")