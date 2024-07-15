from fastapi import APIRouter
from fastapi.responses import JSONResponse

from db.sessions.admin_sessions.add_func import *

add = APIRouter()

def include_CORS(message = { }):
    response = JSONResponse(message)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

@add.post('/device') 
def _(room_number: int, device_status: str):
    add_device(room_number, device_status)
    return include_CORS()

@add.post('/news') 
def _(title: str, description: str, photo_url: str):
    add_news(title, description, photo_url)
    return include_CORS()

@add.post('/about') 
def _(title: str, description: str, photo_url: str):
    add_about(title, description, photo_url)
    return include_CORS()

@add.post('/service')
def _(name: str, description: str, price: int, photo_url: str):
    add_service(name, description, price, photo_url)
    return include_CORS()

@add.post('/guide-category')
def _(title: str, photo_url: str):
    if check_category(title):
        add_guide_category(title, photo_url)
        return include_CORS()
    else: return include_CORS({"error": "Category already exists!"})

@add.post('/city-guide')
def _(placename: str, description: str, address: str, category: str, recommended: int, photo_url: str):
    add_guide(placename, description, address, category, bool(recommended), photo_url)
    return include_CORS()

@add.post('/menu') 
def _(name: str, description: str, price: int, recommended: int, photo_url: str):
    add_menu(name, description, price, bool(recommended), photo_url)
    return include_CORS()

@add.post('/app') 
def _(name: str, resource_url: str, photo_url: str):
    add_app(name, resource_url, photo_url)
    return include_CORS()
