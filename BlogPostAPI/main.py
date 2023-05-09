from fastapi import FastAPI

from logic import *
from models import BlogPost

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Welcome to the blogpost API."}


@app.post('/blogposts/')
def create_blogpost(blog:BlogPost):
    print("*******")
    blogs = Blog(blog)
    return blogs.create_blog()
    
    