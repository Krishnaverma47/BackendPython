from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email:str
    password:str

class UserBaseUpdate(BaseModel):
    name: str
    email:str 


class ShowUser(BaseModel):
    name: str
    email: str  
    class Config:
        orm_mode = True 


class Login(BaseModel):
    username: str
    password: str 



# for JWTtoken genetarte 

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

