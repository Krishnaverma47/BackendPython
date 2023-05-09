from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from fastapi  import Depends,HTTPException,status
from .import schemas 
 
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
 
def create_access_token(data: dict, expires_delta: timedelta = None):
       to_encode = data.copy()
       if expires_delta:
        expire = datetime.utcnow() + expires_delta
       else:
        expire = datetime.utcnow() + timedelta(minutes=15)
       to_encode.update({"exp": expire})
       encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
       return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def decode_access_token(token:str = Depends(oauth2_scheme)):
   credentials_exception = HTTPException(
       status_code=status.HTTP_401_UNAUTHORIZED,
       detail="Could not validate credentials",
       headers={"WWW-Authenticate": "Bearer"},
   )
   try:
       payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
       email: str = payload.get("sub")
       if email is None:
        raise credentials_exception
       token_data = schemas.TokenData(email=email)
   except PyJWTError:
       raise credentials_exception
