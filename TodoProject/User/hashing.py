from passlib.context import CryptContext


from User import models

 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
  
 
def get_password_hash(password):
   return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
   return pwd_context.verify(plain_password, hashed_password)

 
def authenticate_user(db, email: str, password: str)->dict:
   user = db.query(models.User).filter(models.User.email == email).first()
   if not user:
    return {'details':'Credentialsare invalid'}
   if not verify_password(password, user.password):
   	return {'details':'Credentialsare invalid'}
   return user