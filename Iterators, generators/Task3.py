# Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving
# elements using square brackets syntax.

class Counter:
    def __init__(self, start=0):
        self.number = start
        self.list = []

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        self.list.append(self.number)
        return self.list


list_one = Counter()
iter_list_one = iter(list_one)

for i in range(10):
    main_list = next(iter_list_one)
    print(main_list[-1])

