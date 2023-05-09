from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List 
from fastapi.security import OAuth2PasswordRequestForm

from .database import SessionLocal, engine
from . import models,schemas,hashing,JWTtoken,oAuth  

from jose import JWTError, jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users", tags=['Users'])
def create_user(user: schemas.UserBase, db: Session = Depends(get_db))->dict:

    db_user = models.User(name=user.name, email=user.email, hashed_password=hashing.Hash.bcrypt(user.password))
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
        


# @app.get("/users", tags=['Users'])    #response_model=List[schemas.ShowUser]
# def GetAllUserData(db: Session = Depends(get_db),current_user: schemas.UserBase = Depends(oAuth.get_current_user)): #token: str = Depends(oauth2_scheme),
#     users = db.query(models.User).all()

#     return users 


@app.get("/users/{id}", tags=['Users'])
def GetUserDataWithID(id:int, db: Session = Depends(get_db),current_user: schemas.UserBase = Depends(oAuth.get_current_user))->dict:
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=400, detail=f"User with id {id} is not present.")

    return users 


@app.delete("/users/{id}", tags=['Users'])
def delete(id:int, db: Session = Depends(get_db),current_user: schemas.UserBase = Depends(oAuth.get_current_user))->dict:
    users = db.query(models.User).filter(models.User.id == id)
    if not users.first():
        raise HTTPException(status_code=400, detail=f"User with id {id} is not present.")
    users.delete(synchronize_session = False)
    db.commit()
    return {'detail':'User is deleted.'}



@app.put("/users/{id}", tags=['Users'])
def updateData(id:int, request: schemas.UserBaseUpdate, db: Session = Depends(get_db),current_user: schemas.UserBase = Depends(oAuth.get_current_user))->dict:
    users = db.query(models.User).filter(models.User.id == id)
    if not users.first():
        raise HTTPException(status_code=400, detail=f"User with id {id} is not present.")
    users.update(request.dict(), synchronize_session = False)
    db.commit()
    return {'details':f'The blog with {id} is updated'}






@app.post('/login',tags = ['Login'])
def login(request:OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db))->str:
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = 400,detail='Username or Password invalid.')

    databasePassword = user.hashed_password
 
    if not hashing.Hash.verifyPassword(request.password,databasePassword):
        raise HTTPException(status_code = 400,detail='Username or Password invalid.')

    # else raise a jwt token here and return it .

    access_token = JWTtoken.create_access_token(data={"sub": user.email})

    payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    return {'user Details':email,"access_token": access_token, "token_type": "bearer"}

    # return {"access_token": access_token, "token_type": "bearer"}