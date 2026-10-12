"""Greeting functionality."""


def greet(name: str = "world") -> str:
    """Return a friendly greeting for *name*."""
    cleaned_name = name.strip() or "world"
    return f"Hello, {cleaned_name}!"
