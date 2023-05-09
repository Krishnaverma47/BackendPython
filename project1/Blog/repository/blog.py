from fastapi import Depends
from sqlalchemy.orm import Session 
from .. import models,database,schemas


def getAll(db: Session= Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs



def create(request:schemas.Blog,db:Session = Depends(database.get_db)):
    new_blog = models.Blog(title= request.title,body= request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



def blogWithID(id:int ,db:Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail= f'Blog with this {id} is not found')
        
        
        # alternative use of HTTPException is response 
        
        # response.status_code= status.HTTP_404_NOT_FOUND
        # return {'details':f'Blog with this {id} is not found'}
    return blogs



def delete(id:int ,db:Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'The blog {id} is not found.')

    blog.delete(synchronize_session = False)
    db.commit()
    return {'details': f'the blog with the {id} is deleted'}



def updateData(id:int,request:schemas.Blog,db:Session = Depends(database.get_db)):
    blog =db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail = f'Blog with {id} not found')
    
    blog.update(request.dict())
    db.commit()
    return {'details':f'The blog with {id} is updated'}