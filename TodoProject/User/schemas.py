from pydantic import BaseModel
from pydantic import EmailStr


class UserBase(BaseModel):
   email: EmailStr
   class Config:
        orm_mode = True

class UserCreate(UserBase):
   fname: str
   lname: str
   password: str

# for creating the todoapp

class TODOCreate(BaseModel):
   text: str
   completed: bool


# for updating the todoapp
class TODOUpdate(TODOCreate):
   id: int
   
   
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None