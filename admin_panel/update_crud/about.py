from fastapi import APIRouter
import db.sessions.admin_sessions.updates_func.about as edit_about

edit = APIRouter()

@edit.post("/title")
def _(id: int, value: str):
    edit_about.title(id, value)

@edit.post("/description")
def _(id: int, value: str):
    edit_about.description(id, value)

@edit.post("/photo-url")
def _(id: int, value: str):
    edit_about.photo_url(id, value)
