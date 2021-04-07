#-- Python in-built imports --#
from fastapi import Depends, status, Response, APIRouter
from sqlalchemy.orm import Session
from typing import List

#-- User defined imports --#
from .. import schemas, oauth2
from ..database import get_db
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

#-- Create a Blog Post
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session=Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create_blog(request, db)

#-- Get a Blog Post by its id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog) #-- response_model is used to limit the data that will be shown to the user. More details can be found inside schemas.py file
def show(id:int, response:Response, db:Session=Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_blog_by_id(id, db)


#-- Delete a Blog Post
@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def destroy(id:int, db:Session=Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)

#-- Update a Blog Post
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update_blog(id,request, db)
    

#-- Get all the Blog Posts
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all_blogs(db)