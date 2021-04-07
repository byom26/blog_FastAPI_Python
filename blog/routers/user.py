#-- Python in-built imports --#
import re
from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session

#-- User defined imports --#
from .. import schemas,models
from ..database import get_db
from ..repository import user


router = APIRouter(
    prefix="/user",
    tags=['Users']
)

#-- Create a new user
@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db:Session=Depends(get_db)):
    return user.create_user(request, db)

#-- Get the details of a users
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session=Depends(get_db)):
    return user.get_user(id, db)