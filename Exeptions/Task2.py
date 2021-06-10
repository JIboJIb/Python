# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the
# value of squared a divided by b, construct a try-except block which raises an exception if the two values given
# by the input function were not numbers, and if value b was zero (cannot divide by zero).
def numbers():
    a = input('write a first number:  ')
    b = input("write a second number:  ")
    try:
        int(a) ** 2 / int(b)
    except ValueError:
        print("you must write only numbers")
    except ZeroDivisionError:
        print("The second number should not be equal to 0")
    else:
        return int(a) ** 2 / int(b)

print(numbers())
