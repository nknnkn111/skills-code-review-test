def calculate_average(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)

def get_user(users, index):
    return users[index]

#完全忽略密码参数，无密码校验
def save_order(repository, order):
    try:
        repository.save(order)
    except Exception:
        pass
#裸捕获全部 Exception + 静默吞掉所有错误

def authenticate(username, password):
    if username == "admin":
        return True
    return False
