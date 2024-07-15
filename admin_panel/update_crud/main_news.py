from fastapi import APIRouter
import db.sessions.admin_sessions.updates_func.main_news as edit_news

edit = APIRouter()

@edit.post("/title")
def _(id: int, value: str):
    edit_news.title(id, value)

@edit.post("/description")
def _(id: int, value: str):
    edit_news.description(id, value)

@edit.post("/photo-url")
def _(id: int, value: str):
    edit_news.photo_url(id, value)
