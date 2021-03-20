from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

# class ShowBlog(Blog):
    
#     class Config():
#         orm_mode = True

#-- We can either extend the Blog class as above to hide the id from the user
#-- OR We can extend the BaseModel as below to hide the id from the user but here we have to manually declare the fields
#-- Also don't forget to craete the orm_mode Config.

class ShowBlog(BaseModel):
    title: str
    body: str
    
    class Config():
        orm_mode = True

#-- Schemas for User
class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True