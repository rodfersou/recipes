import functools
from typing import Any, Callable


def override_errors(error_response: dict):
    def inner(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception:
                return error_response

        return wrapper

    return inner
