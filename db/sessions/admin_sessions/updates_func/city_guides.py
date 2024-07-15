from db.create_db import create_session
from db.models import CityGuides

session = create_session()

def placename(id: str, placename: str) -> None:
    OBJ = session.query(CityGuides).filter(CityGuides.id == id).scalar()
    OBJ.placename = placename
    session.commit()

def description(id: str, description: str) -> None:
    OBJ = session.query(CityGuides).filter(CityGuides.id == id).scalar()
    OBJ.description = description
    session.commit()

def address(id: str, address: str) -> None:
    OBJ = session.query(CityGuides).filter(CityGuides.id == id).scalar()
    OBJ.address = address
    session.commit()

def recommended(id: str, recommended: bool) -> None:
    OBJ = session.query(CityGuides).filter(CityGuides.id == id).scalar()
    OBJ.recommended = recommended
    session.commit()

def category(id: str, category: str) -> None:
    OBJ = session.query(CityGuides).filter(CityGuides.id == id).scalar()
    OBJ.category = category
    session.commit()

def photo_url(id: str, photo_url: str) -> None:
    OBJ = session.query(CityGuides).filter(CityGuides.id == id).scalar()
    OBJ.photo_url = photo_url
    session.commit()
