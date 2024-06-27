from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@my_decorator
def example_function():
    """This is an example function."""
    print("Inside the example function")

# Using the decorated function
example_function()
