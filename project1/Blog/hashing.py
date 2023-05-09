from passlib.context import CryptContext

class Hash():
    def bcrypt(password:str):
        pwd_cxt =CryptContext(schemes=['bcrypt'],deprecated = 'auto')
        hashedPassword = pwd_cxt.hash(password)
        return hashedPassword