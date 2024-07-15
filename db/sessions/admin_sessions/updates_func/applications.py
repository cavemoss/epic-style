from db.create_db import create_session
from db.models import Applications

session = create_session()

def name(id: int, name: str):
    OBJ = session.query(Applications).filter(Applications.id == id).scalar()
    OBJ.name = name
    session.commit()

def resource_url(id: int, resource_url: str):
    OBJ = session.query(Applications).filter(Applications.id == id).scalar()
    OBJ.resource_url = resource_url
    session.commit()

def photo_url(id: int, photo_url: str):
    OBJ = session.query(Applications).filter(Applications.id == id).scalar()
    OBJ.photo_url = photo_url
    session.commit()