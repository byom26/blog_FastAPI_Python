from pydantic import BaseModel
from typing import List, Optional


class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

# class ShowBlog(Blog):
    
#     class Config():
#         orm_mode = True

#-- We can either extend the Blog class as above to hide the id from the user
#-- OR We can extend the BaseModel as below to hide the id from the user but here we have to manually declare the fields
#-- Also don't forget to craete the orm_mode Config.


#-- Schemas for User
class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None