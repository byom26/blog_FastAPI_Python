from passlib.context import CryptContext


psswdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashPasswd(password):
    return psswdContext.hash(password)