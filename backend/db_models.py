from sqlalchemy import Column, Boolean, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BaseDBModel = declarative_base()

class Job(BaseDBModel):
    __tablename__ = 'tbl_jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    posted_date = Column(Date)
    is_active = Column(Boolean, default=True) 
    owner_id = Column(Integer, ForeignKey('tbl_users.id'))

    owner = relationship('User', back_populates='jobs')

class User(BaseDBModel):
    __tablename__ = 'tbl_users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    jobs = relationship('Job', back_populates='owner') 