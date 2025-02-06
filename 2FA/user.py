#import bcrypt
import pyotp

class User:
    def __init__(self, login, password, otp_secret=None):
        self.login = login
        self.password = password
        self.otp_secret = otp_secret or pyotp.random_base32()

    def verify_password(self, password):
        return self.password == password

    def update_password(self, new_password):
        self.password = new_password  # Aktualizacja hasła

    def to_dict(self):
        return {
            'login': self.login,
            'password': self.password,
            'otp_secret': self.otp_secret
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['login'], data['password'], data['otp_secret'])
    
    def __str__(self):
        return f"User(login='{self.login}')"