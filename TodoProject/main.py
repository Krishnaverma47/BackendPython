from fastapi import FastAPI,Depends,HTTPException,status 
from User import models,schemas,hashing,database,JwtToken
from typing import List
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
ACCESS_TOKEN_EXPIRE_MINUTES = 30


models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()


def get_db():
   """provide db session to path operation functions"""
   try:
       db = database.SessionLocal()
       yield db
   finally:
       db.close() 
       
# @app.get('/api')
# def root(db: Session = Depends(get_db),current_user: schemas.UserBase = Depends(JwtToken.decode_access_token))->dict: #current_user: schemas.UserBase = Depends(JwtToken.decode_access_token)
#     return {'Database':db.query(models.User).all()}

# for signing the user 

@app.post("/api/users",response_model=schemas.UserBase)
def signup(user_data: schemas.UserCreate, db: Session = Depends(get_db))->dict:
    db_user = models.User(fname=user_data.fname,lname =user_data.lname,email=user_data.email,password= hashing.get_password_hash(user_data.password))
    if db.query(models.User).filter(models.User.email == user_data.email).first():
        raise HTTPException(status_code=409,detail="Email already registered.")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/api/login", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db),form_data: OAuth2PasswordRequestForm= Depends()):
   """generate access token for valid credentials"""
   userdata = hashing.authenticate_user(db, form_data.username, form_data.password)
   if not userdata:
   	raise HTTPException(
       	status_code=HTTP_401_UNAUTHORIZED,
       	detail="Incorrect email or password",
       	headers={"WWW-Authenticate": "Bearer"},
   	)
   access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
   access_token = JwtToken.create_access_token(data={"sub": userdata.email},expires_delta=access_token_expires)
   return {"access_token": access_token, "token_type": "bearer"}




# todos related path ------------------------------






if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=5000)
    # uvicorn.run(app, host="localhost", port=8080)