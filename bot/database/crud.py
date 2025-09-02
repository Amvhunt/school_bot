from .models import User, Class
from .connection import SessionLocal

def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

def get_classes():
    db = SessionLocal()
    classes = db.query(Class).all()
    db.close()
    return classes
