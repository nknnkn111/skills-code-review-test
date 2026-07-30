from app.review_cases import (
    authenticate,
    calculate_average,
    get_user,
    save_order,
)


class FailingRepository:
    def save(self, order):
        raise RuntimeError("database connection failed")


def test_calculate_average():
    result = calculate_average([10, 20, 30])

    assert result == 20


def test_get_user():
    users = ["Tom", "Alice", "Bob"]

    result = get_user(users, 1)

    assert result == "Alice"


def test_save_order():
    repository = FailingRepository()
    order = {
        "order_id": 1001,
    }

    result = save_order(repository, order)

    assert result is None


def test_authenticate():
    result = authenticate(
        username="admin",
        password="wrong-password",
    )

    assert result is True