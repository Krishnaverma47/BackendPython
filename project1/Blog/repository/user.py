from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session 
from .. import models,database,schemas,hashing


def create(request: schemas.User,db:Session = Depends(database.get_db)):
    newUser = models.User(name= request.name,email = request.email,password = hashing.Hash.bcrypt(request.password))
    db.add(newUser)
    db.commit()
    return {'detail':'User added to the database'} 

def User(db:Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users 


def getuser(id:int,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = 'user not found the list')
    return user