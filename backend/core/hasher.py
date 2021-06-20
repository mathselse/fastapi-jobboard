from passlib.context import CryptContext

pwdContext = CryptContext(schemes=['bcrypt'], deprecated='auto')

class PasswordHasher():
    @staticmethod
    def verify_hash(self, plain_password, hashed_password):
        return pwdContext.verify(plain_password, hashed_password)

    @staticmethod
    def get_hash(plain_password):
        return pwdContext.hash(plain_password)