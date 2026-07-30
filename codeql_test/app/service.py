from app.database import Database
from app.user import User


class UserService:
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def create_user(self, name):
        user = User(name)

        self.db.save(user.info())

        return user

    def delete_user(self, user_id):
        self.db.delete(user_id)