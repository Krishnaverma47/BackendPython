from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session 
from typing import List
from .. import schemas,models
from ..database import get_db
from ..repository import blog

router = APIRouter(
    prefix = '/blog',
    tags = ['Blogs']
)


@router.get('/',response_model = List[schemas.showBlog])
def allBlogs(db: Session=Depends(get_db)):
    return blog.getAll(db)
    


@router.post('/',status_code = status.HTTP_201_CREATED)
def createBlog(request: schemas.Blog,db: Session=Depends(get_db)):
    return blog.create(request,db)


@router.get('/{id}',status_code = 200,response_model = schemas.showBlog)
def perticularIdBlog(id:int,response:Response,db:Session = Depends(get_db)):
    return blog.blogWithID(id,db)


@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT)
def deleteBlog(id,db:Session = Depends(get_db)):
    return blog.delete(id,db)


@router.put('/{id}',status_code = 200)
def Update(id, request: schemas.Blog, db:Session = Depends(get_db)):
    return blog.updateData(id,request,db)
