from pydantic import BaseModel
from typing import List

class Blog(BaseModel):    
    title: str
    body: str 

class User(BaseModel):
    name: str
    email: str
    password: str


class BlogBase(Blog):    
    class Config:
        orm_mode = True 

class showUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogBase]
    class Config:
        orm_mode = True  

class showBlog(Blog):
    creator: showUser
    class Config:
        orm_mode = True   