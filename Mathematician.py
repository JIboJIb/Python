# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
class Mathematician:
    def square_nums(self, list):
        new_list = []
        for i in list:
            new_list.append(i ** 2)
        return new_list

    def remove_positives(self, list):
        new_list = []
        for i in list:
            if i < 0:
                new_list.append(i)
        return new_list

    def filter_leaps(self, list):
        new_list = []
        for i in list:
            if i % 4 == 0 and i % 100 != 0:
                new_list.append(i)
        return new_list

m = Mathematician()
print(m.square_nums([1,2,3,4,5]))
print(m.remove_positives([1, 1, -2, -3]))
print(m.filter_leaps([2004, 2000, 4, 1882]))
