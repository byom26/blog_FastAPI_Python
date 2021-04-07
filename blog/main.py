#-- Python in-built imports --#
from fastapi import FastAPI

#-- User defined imports --#
from . import database, models
from .routers import blog, user, authentication


app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)





#-- Get a Blog Post by its id
# @app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=['blogs']) #-- response_model is used to limit the data that will be shown to the user. More details can be found inside schemas.py file
# def show(id, response:Response, db:Session=Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'Result': f'Blog with id {id} not available!'}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not available!')
#     return blog

#-- Create a new user
# @app.post('/user', response_model=schemas.ShowUser, tags=['users'])
# def create_user(request:schemas.User, db:Session=Depends(get_db)):
#     new_user = models.User(name=request.name, email=request.email, password=hashPasswd(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user