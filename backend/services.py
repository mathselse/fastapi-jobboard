from sqlalchemy.orm import Session, query
from db_session import SessionLocal, db_engine
import db_models, view_models
from core.hasher import PasswordHasher

def create_db():
    db_models.BaseDBModel.metadata.create_all(bind=db_engine)

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(user: view_models.UserCreate, db: Session):
    new_user = db_models.User(
            username=user.username, 
            email=user.email, 
            hashed_password=PasswordHasher.get_hash(user.password)
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(db_models.User).all()

def create_job(job: view_models.JobCreate, owner_id: int, db: Session):
    new_job = db_models.Job(**job.dict(), owner_id = owner_id)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

def get_jobs(db: Session):
    return db.query(db_models.Job).all()

def get_job_by_id(id: int, db: Session):
    return db.query(db_models.Job).filter(db_models.Job.id == id).first()

def delete_job(id: int, db: Session):
    job = db.query(db_models.Job).filter(db_models.Job.id == id)
    if not job.first():
        return False
    job.delete()
    db.commit()
    return True

def update_job(id: int, job: view_models.JobUpdate, owner_id: int, db: Session):
    existing_job = db.query(db_models.Job).filter(db_models.Job.id == id)
    if not existing_job.first():
        return False
    job.__dict__.update(owner_id=owner_id)
    existing_job.update(job.__dict__)
    db.commit()
    return True