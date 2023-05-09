from passlib.context import CryptContext

class Hash:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def bcrypt(password):
        hashed_password = Hash.pwd_context.hash(password)
        return hashed_password

    # for verifying the password 

    def verifyPassword(plain_password, hashed_password):
        return Hash.pwd_context.verify(plain_password, hashed_password)    