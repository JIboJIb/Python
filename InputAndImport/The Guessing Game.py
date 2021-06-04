# =============================================================================
# Write a program that generates a random number between 1 and 10 and lets
# the user guess what number was generated. The result should be sent back to 
# the user via a print statement.
# =============================================================================

import random
a = random.randint(1, 10)
while True:
    b = input("Guess number between 1-10:  ")
    if b.isdigit():
        if a == int(b):
            print("Good")
            break
        else:
            print("Try again")
    else:
        print("Please write only number between 1-10")
