# Write a Python program to access a function inside a function (Tips: use function, which returns another function)
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    greeting = func("""Text for checking the task""")
    print(greeting)


greet(shout)
greet(whisper)