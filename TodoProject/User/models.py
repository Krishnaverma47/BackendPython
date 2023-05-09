from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
   __tablename__ = "users"
   
   id = Column(Integer, primary_key=True, index=True)
   fname = Column(String)
   lname = Column(String)
   email = Column(String, unique=True, index=True)
   password = Column(String)
   todos = relationship("TODO", back_populates="owner")



class TODO(Base):
   __tablename__ = "todos"
   
   id = Column(Integer, primary_key=True, index=True)
   text = Column(String, index=True)
   completed = Column(Boolean, default=False)
   owner_id = Column(Integer, ForeignKey("users.id"))
   owner = relationship("User", back_populates="todos")