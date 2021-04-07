from sqlalchemy.orm import Session, session
from fastapi import HTTPException, status

from .. import models, schemas


def get_all_blogs(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_blog_by_id(id:int, db:session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not available!')
    return blog

def create_blog(request:schemas.Blog, db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, userID=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} doesnot exists!")
    blog.delete(synchronize_session=False)
    db.commit()
    return f'Blog with id {id} deleted successfully!'

def update_blog(id:int, request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} doesnot exists!")
    # blog.update(request)
    blog.update(dict(request))
    db.commit()
    return "Blog updated successfully!"