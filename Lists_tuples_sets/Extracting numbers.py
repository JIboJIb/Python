# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration
i = 0
list = []
list2 = []
while i < 100:
    list.append(i)
    i += 1
    if i % 7 == 0 and i % 5 != 0:
        list2.append(i)
        i += 1
print(list)
# !!!append і list якщо разом повертають none!!!
print(list2)
