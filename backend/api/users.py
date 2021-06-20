from fastapi import APIRouter, HTTPException
from typing import List
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
import services
from view_models import UserCreate, User

user_routes = APIRouter()

@user_routes.post('/', response_model=User, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(services.get_db_session)):
    new_user = services.create_user(user, db)
    return new_user

@user_routes.get('/', response_model=List[User])
def users(db: Session = Depends(services.get_db_session)):
    users = services.get_users(db)
    if not users:
        raise HTTPException(HTTP_404_NOT_FOUND, detail="No users")
    return users