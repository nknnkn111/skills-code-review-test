class Database:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def save(self, user):
        if not self.connected:
            raise RuntimeError("database is not connected")

        print("save user:", user)

    def delete(self, user_id):
        print("delete user:", user_id)
        