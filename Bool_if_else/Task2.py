number = input("Write a number\n")
while True:
    if number.isdigit() and len(number) == 10:
        print("Good")
        break
    else:
        print("Try again")
        number = input("Write a number with 10 digits and without leters\n")
