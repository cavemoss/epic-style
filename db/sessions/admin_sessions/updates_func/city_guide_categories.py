from db.create_db import create_session
from db.models import CityGuideCategories

session = create_session()

def title(id: int, title:str):
    OBJ = session.query(CityGuideCategories).filter(CityGuideCategories.id == id).scalar()
    OBJ.title = title
    OBJ.fk = title
    session.commit()

def photo_url(id: int, photo_url: str):
    OBJ = session.query(CityGuideCategories).filter(CityGuideCategories.id == id).scalar()
    OBJ.photo_url = photo_url
    session.commit()
