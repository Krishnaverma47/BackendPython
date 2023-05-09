from pydantic import BaseModel,Field, EmailStr
from datetime import date
from bson import ObjectId
import json


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
        
    @classmethod
    def validate(cls,v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    
    @classmethod
    def __modify_schema__(cls,field_schema):
        field_schema.update(type="string")

class Admin(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId,alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    dob: str = Field(...)
    hashed_password: str = Field(...)
    isActive: bool = True
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True #required for the _id 
        json_encoders = {ObjectId: str}
        
        schema_extra = {
            "example": {
                "name": "Krishna Verma",
                'email':'krishna10799@gmail.com',
                "dob":"1990-01-01",
                'hashed_password':'Krishna1234$',
                'isActive':True
            }
        }

class Student(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId,alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    roll_number: int = Field(unique= True)
    dob: str = Field(...)
    isActive: bool = True

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True #required for the _id 
        json_encoders = {ObjectId: str}
        
        schema_extra = {
            "example": {
                "name": "Krishna Verma",
                'email':'krishna10799@gmail.com',
                'roll_number':12,
                "dob":"1990-01-01",
                'isActive':True
            }
        }    
        
class Book(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId,alias="_id")
    book_name: str = Field(...)
    author_name: str = Field(...)
    publication: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True #required for the _id 
        json_encoders = {ObjectId: str}
        
        schema_extra = {
            "example": {
                "book_name":"Mathematics II",
                "author_name":"Ramanujan",
                "publication":"PNB Publication"
            }
        }


class TokenData(BaseModel):
    username: str | None = None
    

