def exception_handling(func):
    def my_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f"function result: {func.__name__}: {result}")
            return result
        except Exception as e:
            print(f"Exception caught in {func.__name__}: {e}")
            return None
    return my_func


@exception_handling
def divide(a, b):
    return a / b
print(divide(5, 0))
