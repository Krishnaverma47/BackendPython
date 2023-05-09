from pydantic import BaseModel,EmailStr,Field
from bson import ObjectId

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


class BlogPost(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId,alias="_id")
    title: str
    content: str
    author: str
    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        
        schema_extra = {
            "example": {
                "title": "Namaste India",
                'content':'Hello you are in beautiful country.',
                'author':"Krishna Verma"
            }
        }
    
    
class User(BaseModel):
    id: ObjectId
    name: str
    email: EmailStr
    password: str
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}