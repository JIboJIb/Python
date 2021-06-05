# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
import random
list = []
i = 0
while i <10:
    list.append(random.randrange(1,100))
    i+=1
print(list)
print(f"The greatest number of the list: {max(list)} ")
