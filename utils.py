"""Utils function."""
import functools
import time

from typing import List, Dict, Any, Callable


def timer(func):
    """Loging function run time."""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start_time = time.perf_counter()
        value = func()
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_decorator


def run(test_cases: List[Dict[str, Any]], func: Callable[[Any], Any]):
    for test_case in test_cases:
        result = func(**test_case["input"])
        expected = test_case["ans"]
        if result != expected:
            raise AssertionError(f"input: {test_case['input']}, want: {expected}, but get {result}") # noqa