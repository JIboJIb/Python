# Create your own implementation of a built-in function enumerate,
# named 'with_index', which takes two parameters: 'iterable' and
# 'start', default is 0. Tips: see the documentation for the enumerate function.
actions = ["eat", "sleep", "repeat"]

def with_index(iterable, start=0):
    n = start
    for elem in iterable:
        print(n, elem)
        n += 1

print(with_index(actions))
