# Write a program that reads in a sequence of characters and prints them in reverse order, using
# your implementation of Stack.
# stack = []
# new_stack = []
# i = 1
# while i <= 5:
#     stack.append(i)
#     i += 1
# print(stack)
# for item in stack:
#     new_stack.append(stack.pop())
# print(new_stack)
# class Stack:
#     def __init__(self):
#         self.elements = []
#
#     def push(self, value):
#         self.elements.append(value)
#
#     def pop(self):
#         return self.elements.pop()
#
#     def empty(self):
#         return self.elements == []
#
#     def show(self):
#         for value in reversed(self.elements):
#             print(value)
#
#
# def bottom_insert(s, value):
#     if s.empty():
#         s.push(value)
#     else:
#         popped = s.pop()
#         bottom_insert(s, value)
#         s.push(popped)
#
#
# def reverse(s):
#     if s.empty():
#         pass
#     else:
#         popped = s.pop()
#         reverse(s)
#         bottom_insert(s, popped)
#
#
# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# my_stack.push(4)
# my_stack.push(5)
# print(my_stack.show())
# print(reverse(my_stack))
def createStack():
    stack = []
    return stack


# Function to determine the size of the stack
def size(stack):
    return len(stack)


# Stack is empty if the size is 0
def isEmpty(stack):
    if size(stack) == 0:
        return True


# Function to add an item to stack .
# It increases size by 1
def push(stack, item):
    stack.append(item)


# Function to remove an item from stack.
# It decreases size by 1
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()


# A stack based function to reverse a string
def reverse(string):
    n = len(string)

    # Create a empty stack
    stack = createStack()

    # Push all characters of string to stack
    for i in range(0, n, 1):
        push(stack, string[i])

    # Making the string empty since all
    # characters are saved in stack
    string = ""

    # Pop all characters of string and
    # put them back to string
    for i in range(0, n, 1):
        string += pop(stack)

    return string


# Driver program to test above functions
string = "GeeksQuiz"
string = reverse(string)
print("Reversed string is " + string)
