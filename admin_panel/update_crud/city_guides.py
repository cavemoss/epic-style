from fastapi import APIRouter
import db.sessions.admin_sessions.updates_func.city_guides as edit_guides

edit = APIRouter()

@edit.post("/placename")
def _(id: int, value: str):
    edit_guides.placename(id, value)

@edit.post("/description")
def _(id: int, value: str):
    edit_guides.description(id, value)

@edit.post("/address")
def _(id: int, value: str):
    edit_guides.address(id, value)

@edit.post("/recommended")
def _(id: int, value: int):
    edit_guides.recommended(id, bool(value))

@edit.post("/category")
def _(id: int, value: str):
    edit_guides.category(id, value)

@edit.post("/photo-url")
def _(id: int, value: str):
    edit_guides.photo_url(id, value)
