# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
def logger(function):
    def args_function(* args):
        return f"{function.__name__} called with {args}"
    return args_function

@logger
def add(x, y):
    return x + y

@logger
def square_all(* args):
    return [arg ** 2 for arg in args]


add_one = add(4, 5)
print(add_one)
square = square_all(4, 5, 6)
print(square)