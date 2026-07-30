from typing import Sequence


def calculate_average(numbers: Sequence[float]) -> float:
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)


def get_user(users: Sequence[str], index: int) -> str | None:
    if index < 0 or index >= len(users):
        return None

    return users[index]


def authenticate(
    username: str,
    password: str,
    expected_password: str,
) -> bool:
    return username == "admin" and password == expected_password


def save_order(repository, order) -> None:
    repository.save(order)
