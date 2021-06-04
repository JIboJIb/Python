# =============================================================================
# Write a program that asks the answer for a mathematical expression, checks 
# whether the user is right or wrong, and then responds with a message 
# accordingly.
# =============================================================================
import random
i = 0
a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
expression1 = a + b - c
expression2 = a + c * b
expression3 = (c + b) * a
print(f"{a}+{b}-{c}")
answer1 = input("your answer :  ")
while True:
    if answer1.isalpha():
        print("It`s not serios write a number")
        answer1 = input("your answer :  ")
    elif int(answer1) == int(expression1):
        print("Well done! Next")
        i = i + 1
        break
    else:
        print("Wrong! Pay attention next time")
        break
print(f"{a}+{c}*{b}")
answer2 = input("your answer :  ")
while True:
    if answer2.isalpha():
        print("It`s not serios write a number")
        answer2 = input("your answer :  ")
    elif int(answer2) == int(expression2):
        print("Well done! Next")
        i = i + 1
        break
    else:
        print("Wrong! Pay attention next time")
        break
print(f"({c}+{b})*{a}")
answer3 = input("your answer :  ")
while True:
    if answer3.isalpha():
        print("It`s not serios write a number")
        answer1 = input("your answer :  ")
    elif int(answer3) == int(expression3):
        print("Well done! Next")
        i = i + 1
        break
    else:
        print("Wrong! Pay attention next time")
        print(f"{a}+{c}*{b}")
        break
print(f"you scored {i} points out of 3")