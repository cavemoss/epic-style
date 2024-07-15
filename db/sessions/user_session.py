from db.models import *
from db.create_db import create_session

session = create_session()


def get_all_devices(): return session.query(
    Devices.id, 
    Devices.room_number, 
    Devices.device_status
).all()

def get_all_news(): return session.query(
    MainNews.id, 
    MainNews.title, 
    MainNews.description, 
    MainNews.photo_url
).all()

def get_all_about(): return session.query(
    About.id, 
    About.title,
    About.description, 
    About.photo_url
).all()

def get_all_services(): return session.query(
    HotelServices.id, 
    HotelServices.name,
    HotelServices.description, 
    HotelServices.price, 
    HotelServices.photo_url
).all()

def get_all_categories(): return session.query(
    CityGuideCategories.id,
    CityGuideCategories.fk,
    CityGuideCategories.title, 
    CityGuideCategories.photo_url,
).all()

def get_all_guides(fk: str = None): return session.query(
    CityGuides.id, 
    CityGuides.placename, 
    CityGuides.description, 
    CityGuides.address, 
    CityGuides.recommended,
    CityGuides.photo_url,
    None if fk else CityGuides.category
).filter((CityGuides.category==fk) if fk is not None else True)

def get_restaurant_menu(): return session.query(
    Restaurant.id, 
    Restaurant.name, 
    Restaurant.description, 
    Restaurant.price, 
    Restaurant.recommended,
    Restaurant.photo_url
).all()

def get_all_recommendations():
    guides = session.query(
        CityGuides.id, 
        CityGuides.placename, 
        CityGuides.photo_url
    ).filter(CityGuides.recommended==True).all()

    restaurant = session.query(
        Restaurant.id, 
        Restaurant.name, 
        Restaurant.photo_url
    ).filter(Restaurant.recommended==True).all()

    return (
        [tuple(('guide',) + tuple(row)) for row in guides] + 
        [tuple(('menu',) + tuple(row)) for row in restaurant]
    )

def get_all_applications(): return session.query(
    Applications.id, 
    Applications.name, 
    Applications.resource_url, 
    Applications.photo_url
).all()
