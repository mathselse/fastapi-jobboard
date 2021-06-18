from database import db_engine
from models import Base

def create_db():
    Base.metadata.create_all(bind=db_engine)
