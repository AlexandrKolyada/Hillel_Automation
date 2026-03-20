def logger(func):
    def inner_func(*args, **kwargs):

        print(f"call function with arguments :{args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"function result: {func.__name__}: {result}")
        return result
    return inner_func


@logger
def add(a, b):
    return a + b

#add(5, 17)
print(add(5, 17))