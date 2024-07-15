import shutil
from dotenv import load_dotenv
import os

from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from jinja_config import templates

from admin_panel.add_crud import add
from admin_panel.delete_crud import delete_api
from admin_panel.update_routes import edit

from db.sessions.user_session import *


# Router Setup
admin = APIRouter()
admin.include_router(add, prefix="/add")
admin.include_router(delete_api, prefix="/delete")
admin.include_router(edit, prefix="/edit")

# Configuration
admin.mount("/static", StaticFiles(directory="static"), name="static")
load_dotenv()
SEVER_URL = f"http://{os.getenv('SERVER_HOST')}:{os.getenv('SERVER_PORT')}"


# Admin Panel Views
class TemplateContext: 

    def __table(self, page_name: str, row: list): return {
        'devices' : lambda: { 'ID':row[0], 'ROOM':row[1], 'STATUS':row[2] },
        'news' : lambda: { 'ID':row[0], 'TITLE':row[1], 'DESC':row[2], 'PICTURE':row[3] },
        'about' : lambda: { 'ID':row[0], 'TITLE':row[1], 'DESC':row[2], 'PICTURE':row[3] },
        'services' : lambda: { 'ID':row[0], 'NAME':row[1], 'DESC':row[2], 'PRICE':row[3], 'PICTURE':row[4] },
        'guide-categories' : lambda: { 'ID':row[0], 'TITLE':row[2], 'PICTURE':row[3] },
        'guides' : lambda: { 'ID':row[0], 'NAME':row[1], 'DESC':row[2], 'ADDRESS':row[3], 'RECOMMENDED':row[4], 'PICTURE':row[5], 'CATEGORY':row[6] },
        'menu' : lambda: { 'ID':row[0], 'NAME':row[1], 'DESC':row[2], 'PRICE':row[3], 'RECOMMENDED':row[4], 'PICTURE':row[5] },
        'apps' : lambda: { 'ID':row[0], 'NAME':row[1], 'URL':row[2], 'PICTURE':row[3] }
    }.get(page_name)() 

    def __style(self, page_name: str): return {
        'devices' : lambda: { 'highlight':page_name, 'columns':'30px repeat(2, 1fr) 60px 110px' },
        'news' : lambda: { 'highlight':page_name, 'columns':'30px repeat(3, 1fr) 60px 110px' },
        'about' : lambda: { 'highlight':page_name, 'columns':'30px repeat(3, 1fr) 60px 110px' },
        'services' : lambda: { 'highlight':page_name, 'columns':'30px repeat(4, 1fr) 60px 110px' },
        'guide-categories' : lambda: { 'highlight':page_name, 'columns':'30px repeat(2, 1fr) 60px 110px' },
        'guides' : lambda: { 'highlight':page_name, 'columns':'30px repeat(6, 1fr) 60px 110px' },
        'menu' : lambda: { 'highlight':page_name, 'columns':'30px repeat(5, 1fr) 60px 110px' },
        'apps' : lambda: { 'highlight':page_name, 'columns':'30px repeat(3, 1fr) 60px 110px' }
    }.get(page_name)() 

    def __init__(self, request: Request, 
        page_context: tuple, 
        postCRUD: str,
        deleteCRUD: str,
        updateCRUD: dict
    ) -> None:
        
        self.request = request
        self.this_page = page_context[0]

        self.table = [dict(self.__table(page_context[0], row)) for row in page_context[1]]
        self.style = self.__style(page_context[0])

        self.postCRUD = postCRUD
        self.deleteCRUD = deleteCRUD
        self.updateCRUD = updateCRUD
        self.media_upload_api = SEVER_URL + '/admin/upload-media'

    def to_dict(self): return {
        **self.__dict__, 
        'fk': [row[1] for row in get_all_categories()] 
        if self.this_page == 'guides' else None
    }


@admin.get('/')
def _(): return RedirectResponse(url='/admin/devices')
delete_api = SEVER_URL + "/admin/delete"
post_api = SEVER_URL + "/admin/add"
update_api = SEVER_URL + "/admin/edit"


@admin.get('/devices')
def _(request: Request): return templates.TemplateResponse('admin/table-view.html', TemplateContext(
    request=request,
    page_context=('devices', get_all_devices()),
    postCRUD=post_api + '/device?room_number={NEW_ROOM}&device_status={NEW_STATUS}',
    deleteCRUD=delete_api + '/device?id={EVENT_TARGET_ID}',
    updateCRUD={ 
        'room' : update_api + '/device/room-number?id={ID}&value={VALUE}',
        'status' : update_api + '/device/device-status?id={ID}&value={VALUE}',
    }
).to_dict())


@admin.get('/news')
def _(request: Request): return templates.TemplateResponse('admin/table-view.html', TemplateContext(
    request=request,
    page_context=('news', get_all_news()),
    postCRUD=post_api + '/news?title={NEW_TITLE}&description={NEW_DESC}&photo_url={NEW_PICTURE}',
    deleteCRUD=delete_api + '/news?id={EVENT_TARGET_ID}',
    updateCRUD={
        'name' : update_api + '/news/title?id={ID}&value={VALUE}',
        'desc' : update_api + '/news/description?id={ID}&value={VALUE}',
        'picture' : update_api + '/news/photo-url?id={ID}&value={VALUE}'
    }
).to_dict())


@admin.get('/about')
def _(request: Request): return templates.TemplateResponse('admin/table-view.html', TemplateContext(
    request=request,
    page_context=('about', get_all_about()),
    postCRUD=post_api + '/about?title={NEW_TITLE}&description={NEW_DESC}&photo_url={NEW_PICTURE}',
    deleteCRUD=delete_api + '/about?id={EVENT_TARGET_ID}',
    updateCRUD={ 
        'name' : update_api + '/about/title?id={ID}&value={VALUE}',
        'desc' : update_api + '/about/description?id={ID}&value={VALUE}',
        'picture' : update_api + '/about/photo-url?id={ID}&value={VALUE}'
    }
).to_dict())


@admin.get('/services')
def _(request: Request): return templates.TemplateResponse('admin/table-view.html', TemplateContext(
    request=request,
    page_context=('services', get_all_services()),
    postCRUD=post_api + '/service?name={NEW_NAME}&description={NEW_DESC}&price={NEW_PRICE}&photo_url={NEW_PICTURE}',
    deleteCRUD=delete_api + '/service?id={EVENT_TARGET_ID}',
    updateCRUD={ 
        'name' : update_api + '/service/name?id={ID}&value={VALUE}',
        'desc' : update_api + '/service/description?id={ID}&value={VALUE}',
        'price' : update_api + '/service/price?id={ID}&value={VALUE}',
        'picture' : update_api + '/service/photo-url?id={ID}&value={VALUE}'
    }
).to_dict())


@admin.get('/guide-categories')
def _(request: Request): return templates.TemplateResponse('admin/table-view.html', TemplateContext(
    request=request,
    page_context=('guide-categories', get_all_categories()),
    postCRUD=post_api + '/guide-category?title={NEW_TITLE}&photo_url={NEW_PICTURE}',
    deleteCRUD=delete_api + '/guide-category?id={EVENT_TARGET_ID}',
    updateCRUD={ 
        'name' : update_api + '/guide-category/title?id={ID}&value={VALUE}',
        'picture' : update_api + '/guide-category/photo-url?id={ID}&value={VALUE}'
    }
).to_dict())


@admin.get('/guides')
def _(request: Request): return templates.TemplateResponse('admin/table-view.html', TemplateContext(
    request=request,
    page_context=('guides', get_all_guides()),
    postCRUD=post_api + '/city-guide?placename={NEW_NAME}&description={NEW_DESC}&address={NEW_ADDRESS}&category={NEW_CATEGORY}&recommended={NEW_RECOMMENDED}&photo_url={NEW_PICTURE}',
    deleteCRUD=delete_api + '/city-guide?id={EVENT_TARGET_ID}',
    updateCRUD={ 
        'name' : update_api + '/guide/placename?id={ID}&value={VALUE}',
        'desc' : update_api + '/guide/description?id={ID}&value={VALUE}',
        'address' : update_api + '/guide/address?id={ID}&value={VALUE}',
        'recommend' : update_api + '/guide/recommended?id={ID}&value={VALUE}',
        'category' : update_api + '/guide/category?id={ID}&value={VALUE}',
        'picture' : update_api + '/guide/photo-url?id={ID}&value={VALUE}'
    }
).to_dict())


@admin.get('/menu')
def _(request: Request): return templates.TemplateResponse('admin/table-view.html', TemplateContext(
    request=request,
    page_context=('menu', get_restaurant_menu()),
    postCRUD=post_api + '/menu?name={NEW_NAME}&description={NEW_DESC}&price={NEW_PRICE}&recommended={NEW_RECOMMENDED}&photo_url={NEW_PICTURE}',
    deleteCRUD=delete_api + '/menu?id={EVENT_TARGET_ID}',
    updateCRUD={ 
        'name' : update_api + '/restaurant/name?id={ID}&value={VALUE}',
        'desc' : update_api + '/restaurant/description?id={ID}&value={VALUE}',
        'price' : update_api + '/restaurant/price?id={ID}&value={VALUE}',
        'recommend' : update_api + '/restaurant/recommended?id={ID}&value={VALUE}',
        'picture' : update_api + '/restaurant/photo-url?id={ID}&value={VALUE}'
    }
).to_dict())


@admin.get('/apps')
def _(request: Request): return templates.TemplateResponse('admin/table-view.html', TemplateContext(
    request=request,
    page_context=('apps', get_all_applications()),
    postCRUD=post_api + '/app?name={NEW_NAME}&resource_url={NEW_URL}&photo_url={NEW_PICTURE}',
    deleteCRUD=delete_api + '/app?id={EVENT_TARGET_ID}',
    updateCRUD={
        'name' : update_api + '/app/name?id={ID}&value={VALUE}',
        'url' : update_api + '/app/resource-url?id={ID}&value={VALUE}',
        'picture' : update_api + '/app/photo-url?id={ID}&value={VALUE}'
    }
).to_dict())


def include_CORS():
    response = JSONResponse({ })
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response


@admin.post('/upload-media')
def _(photo: UploadFile = File(...)):
    if photo.content_type not in ['image/jpeg', 'image/png']:
        return {'error': 'Unsupported file type'}
    path = f'static/media/{photo.filename}'
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(photo.file, buffer)
    return include_CORS()
