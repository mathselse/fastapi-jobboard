from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from core.config import settings
import services
from view_models import JobCreate, Job, JobUpdate
import api.users

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

services.create_db()

@app.include_router(api.users.user_routes, prefix="/users")

@app.get('/')
def hello():
    return "hello world"


    

@app.post('/jobs', response_model=Job, status_code=201)
def create_job(job: JobCreate, db: Session = Depends(services.get_db_session)):
    new_job = services.create_job(job=job, owner_id=1,db=db)
    return new_job

@app.get('/jobs', response_model=List[Job])
def jobs(db: Session = Depends(services.get_db_session)):
    return services.get_jobs(db)

@app.get('/jobs/{id}', response_model=Job)
def job(id: int, db: Session = Depends(services.get_db_session)):
    job = services.get_job_by_id(id, db)
    if job is None:
        raise HTTPException(HTTP_404_NOT_FOUND, detail=f'Job {id} does not exist')
    return job

@app.delete('/jobs/{id}', status_code=204)
def delete_job(id: int, db: Session = Depends(services.get_db_session)):
    if services.delete_job(id, db):
        return
    raise HTTPException(HTTP_404_NOT_FOUND, detail=f'Job {id} is not not existed')

@app.put('/jobs/{id}', status_code=200)
def update_job(id: int, job: JobUpdate, db: Session = Depends(services.get_db_session)):
    updated_job = services.update_job(id, job, 2, db)
    if updated_job == False:
        raise HTTPException(HTTP_404_NOT_FOUND, detail=f'Job {id} is not not existed')
    return job
    



