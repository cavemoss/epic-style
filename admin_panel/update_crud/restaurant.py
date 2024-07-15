from fastapi import APIRouter
import db.sessions.admin_sessions.updates_func.restaurant as edit_restaurant

edit = APIRouter()

@edit.post("/name")
def _(id: int, value: str):
    edit_restaurant.name(id, value)

@edit.post("/description")
def _(id: int, value: str):
    edit_restaurant.description(id, value)

@edit.post("/price")
def _(id: int, value: int):
    edit_restaurant.price(id, value)

@edit.post("/recommended")
def _(id: int, value: int):
    edit_restaurant.recommended(id, bool(value))

@edit.post("/photo-url")
def _(id: int, value: str):
    edit_restaurant.photo_url(id, value)
