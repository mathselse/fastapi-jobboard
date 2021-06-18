from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

db_url = settings.DB_URL
db_engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

