from hello_project import greet


def test_greet_with_name() -> None:
    assert greet("Gouri") == "Hello, Gouri!"


def test_greet_uses_world_by_default() -> None:
    assert greet() == "Hello, world!"


