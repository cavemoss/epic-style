from fastapi import APIRouter
import db.sessions.admin_sessions.updates_func.city_guide_categories as edit_guide_categories

edit = APIRouter()

@edit.post("/title")
def _(id: int, value: str):
    edit_guide_categories.title(id, value)

@edit.post("/photo-url")
def _(id: int, value: str):
    edit_guide_categories.photo_url(id, value)
