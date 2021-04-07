from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()
#-- To start the local server => uvicorn main:app --reload

@app.get('/blog')
def index(limit:int=10, published:bool=True, sort:Optional[str]=None):
    if published:
        return {'data': f"{limit} published blog list from DB"}
    else:
        return {'data': f"{limit} unpublished blog list from DB"}

#-- Here the unpublished function need to be written above the show function beacuse of Dynamic routing --#
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'Unpublished'}

@app.get('/blog/{id}')
def show(id:int):
    #-- Fetch a blog with the id --#
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': [1,2,3,4]}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created with title as {request.title}'}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)