# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers
import random
list1 = []
list2 = []
list_identical = []
i = 0
while i < 10:
    list1.append(random.randrange(1, 10))
    list2.append(random.randrange(1, 10))
    i += 1
print(list1)
print(list2)
list1_modified = set(list1)
list2_modified = set(list2)
# Перетворюєм список у множини щоб знайти одинакові числа без повторів set()
list_identical = list(list1_modified & list2_modified)
# & для пошуку спільних об'єктів https://www.programiz.com/python-programming/set
# list() перетворюємо в список
print(list_identical)
