class User:
    def __init__(self, name):
        self.name = name

    def info(self):
        return {
            "name": self.name,
        }