# Write a class TypeDecorators which has several methods for converting results of functions to a specified type
# (if it's possible):
# methods:
# to_int
# to_str
# to_bool
# to_float

from functools import wraps


class TypeDecorators:

    @classmethod  # метод to_int змінює тип
    def to_(cls, type_):
        def transform(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
                try:
                    value = type_(*args, **kwargs)
                    print(value, type(value))
                except ValueError:
                    print(f'It is not possible to convert the result into {type_}!')
            return wrapper
        return transform


@TypeDecorators.to_(int)
def do_nothing(string):
    return string


@TypeDecorators.to_(bool)
def do_something(string):
    return string


