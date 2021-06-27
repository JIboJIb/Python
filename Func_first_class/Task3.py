# Write a function called `choose_func` which takes a list of nums and 2 callback functions. If all nums inside the
# list are positive, execute the first function on that list and return the result of it. Otherwise, return the result
# of the second one
def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if int(num) > 0]


def choose_func(nums, func1, func2):
    numbers_of_negative = 0
    for num in nums:
        if num < 0:
            numbers_of_negative += 1
    if numbers_of_negative == 0:
        return func1(nums)
    else:
        return func2(nums)


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))
