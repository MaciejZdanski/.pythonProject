import json
import pyotp
from user import User

class AuthenticationSystem:
    def __init__(self, db_file):
        self.db_file = db_file
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.db_file, 'r') as file:
                return {u['login']: User.from_dict(u) for u in json.load(file)}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self):
        with open(self.db_file, 'w') as file:
            json.dump([user.to_dict() for user in self.users.values()], file)

    def register_user(self, login, password):
        if login in self.users:
            raise ValueError("User already exists")
        self.users[login] = User(login, password)
        self.save_users()

    def authenticate_user(self, login, password):
        user = self.users.get(login)
        if user and user.password == password:
            otp = pyotp.TOTP(user.otp_secret).now()
            return otp
        return None

    def update_password(self, login, new_password):
        user = self.users.get(login)
        if user:
            user.password = new_password
            self.save_users()

    def delete_user(self, login):
        if login in self.users:
            del self.users[login]
            self.save_users()
