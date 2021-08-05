# Create your own implementation of a built-in function range, named in_range(), which takes three parameters: `start`,
# `end`, and optional step. Tips: See the documentation for `range` function

def in_range(start, end, step):
    i = start
    if end > start:
        while i < end:
            yield i
            i += step
    elif step < 0:
        while i > end:
            yield i
            i += step


print(list(in_range(1, 10, 1)))
print(list(in_range(0, -10, -1)))
