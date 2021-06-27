# Write a Python program to detect the number of local variables declared in a function.
def sum_of_variables(a):
    b = 5
    return a + b


print(f"number of local variables declared in a function is {sum_of_variables.__code__.co_nlocals}")
