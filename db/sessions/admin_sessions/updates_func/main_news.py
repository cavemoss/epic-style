from db.create_db import create_session
from db.models import MainNews

session = create_session()

def title(id: int, title: str):
    OBJ = session.query(MainNews).filter(MainNews.id == id).scalar()
    OBJ.title = title
    session.commit()

def description(id: int, description: str):
    OBJ = session.query(MainNews).filter(MainNews.id == id).scalar()
    OBJ.description = description
    session.commit()

def photo_url(id: int, photo_url: str):
    OBJ = session.query(MainNews).filter(MainNews.id == id).scalar()
    OBJ.photo_url = photo_url
    session.commit()