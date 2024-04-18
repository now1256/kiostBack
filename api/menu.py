from typing import List

from fastapi import APIRouter, Depends, HTTPException

from database.orm import Menu
from database.repository import MenuRepository
from schema.request import MenuRequest, CreateMenuRequest
from schema.resopnse import MenuSchema, MenuListSchema

router = APIRouter(prefix="/menus")

@router.get("",status_code=200)
def get_menu_handler(
        menu_repo: MenuRepository = Depends()
) -> MenuListSchema:
    menus:List[Menu] = menu_repo.get_menus()
    print(menus)
    if menus:
        return MenuListSchema(
            menus = [MenuSchema.from_orm(menu) for menu in menus]
        )
    raise HTTPException(status_code=404, detail="menu Not Found")

@router.get("/{menu_id}", status_code=200)
def get_menus_handler(
    menu_id : int ,
    menu_repo: MenuRepository = Depends(),
)-> MenuSchema :
    menu : Menu | None = menu_repo.get_menu_by_menu_id(menu_id)
    if menu:
        return MenuSchema.from_orm(menu)
    raise HTTPException(status_code=404, detail="menu Not Found")

@router.post("/menus", status_code=201)
def post_menus_handler(
        request: CreateMenuRequest,
        menu_repo : MenuRepository = Depends()
)-> MenuSchema :
    menu: Menu = Menu.create(request = request)
    menu: Menu = menu_repo.create_menu(menu = menu)
    return MenuSchema.from_orm(menu)

