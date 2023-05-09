from fastapi import HTTPException

from models import BlogPost
from database import db


class Blog:
    def __init__(self, blog: BlogPost):
        self.blog = blog
        
    def create_blog(self):
        # try:
        blog_dict = self.blog.dict() 
        result = db.blogs.insert_one(blog_dict)
        blog_dict['_id'] = str(result.inserted_id)
        return blog_dict
        # except:
        #     raise HTTPException(status_code=404, detail="Something is going wrong.")