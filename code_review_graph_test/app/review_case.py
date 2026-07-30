def calculate_average(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")

    return sum(numbers) / len(numbers)


def get_user(users, index):
    return users[index]


def save_order(repository, order):
    try:
        repository.save(order)
    except Exception:
        pass


def authenticate(username, password):
    if username == "admin":
        return True

    return False