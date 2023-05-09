from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session 
from typing import List
from .. import schemas,models
from ..database import get_db
from ..repository import user


router = APIRouter(
    prefix = '/user',
    tags = ['Users']
)

@router.post('/',status_code= status.HTTP_201_CREATED)
def createUser(request: schemas.User,db:Session = Depends(get_db)):
    return user.create(request,db)



@router.get('/',response_model = List[schemas.showUser])
def getUseAll(db: Session = Depends(get_db) ):
    return user.User(db)



@router.get('/{id}',response_model = schemas.showUser)
def getUser(id,db: Session = Depends(get_db) ):
    return user.getuser(id,db)