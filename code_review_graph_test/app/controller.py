from app.service import UserService


class UserController:
    def __init__(self):
        self.service = UserService()

    def create(self, name):
        return self.service.create_user(name)

    def delete(self, user_id):
        self.service.delete_user(user_id)