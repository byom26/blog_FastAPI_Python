from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List

from starlette.status import HTTP_404_NOT_FOUND

from . import schemas,models
from .database import engine, sessionLocal
from .hashing import hashPasswd


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

#-- Create a Blog Post
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

#-- Delete a Blog Post
@app.delete('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def destroy(id, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} doesnot exists!")
    blog.delete(synchronize_session=False)
    db.commit()
    return f'Blog with id {id} deleted successfully!'

#-- Update a Blog Post
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} doesnot exists!")
    blog.update(request)
    db.commit()
    return "Blog updated successfully!"

#-- Get all the Blog Posts
@app.get('/blog', response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

#-- Get a Blog Post by its id
@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog) #-- response_model is used to limit the data that will be shown to the user. More details can be found inside schemas.py file
def show(id, response:Response, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Result': f'Blog with id {id} not available!'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not available!')
    return blog

#-- Create a new user
@app.post('/user', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db:Session=Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hashPasswd(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#-- Get the details of a users
@app.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} doesn't exists!")
    return user