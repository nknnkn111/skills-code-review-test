from app.controller import UserController


def test_create_user():
    controller = UserController()

    user = controller.create("Tom")

    assert user.name == "Tom"


def test_delete_user():
    controller = UserController()

    controller.delete(1)