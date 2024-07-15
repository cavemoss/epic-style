from fastapi import APIRouter
import db.sessions.admin_sessions.updates_func.applications as edit_applications

edit = APIRouter()

@edit.post("/name")
def _(id: int, value: str):
    edit_applications.name(id, value)

@edit.post("/resource-url")
def _(id: int, value: str):
    edit_applications.resource_url(id, value)

@edit.post("/photo-url")
def _(id: int, value: str):
    edit_applications.photo_url(id, value)
