from db.create_db import create_session
from db.models import Restaurant

session = create_session()

def name(id: int, name: str) -> None:
    OBJ = session.query(Restaurant).filter(Restaurant.id == id).scalar()
    OBJ.name = name
    session.commit()

def description(id: int, description: str) -> None:
    OBJ = session.query(Restaurant).filter(Restaurant.id == id).scalar()
    OBJ.description = description
    session.commit()

def price(id: int, price: int) -> None:
    OBJ = session.query(Restaurant).filter(Restaurant.id == id).scalar()
    OBJ.price = price
    session.commit()

def recommended(id: int, recommended: bool) -> None:
    OBJ = session.query(Restaurant).filter(Restaurant.id == id).scalar()
    OBJ.recommended = recommended
    session.commit()

def photo_url(id: int, photo_url: str) -> None:
    OBJ = session.query(Restaurant).filter(Restaurant.id == id).scalar()
    OBJ.photo_url = photo_url
    session.commit()
