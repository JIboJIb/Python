# Write a program that reads in a sequence of characters, and determines whether
# it's parentheses, braces, and curly brackets are "balanced."
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if self.stack:
            return False
        else:
            return True


def checkBalance(string):
    rec = {')': '(', ']': '[', '}': '{'}
    stack = Stack()

    for char in string:
        if char in ['(', '[', '{']:
            stack.push(char)
        elif char in [')', ']', '}']:
            if stack.isEmpty():
                return 'The string is not balanced.'
            if stack.pop() != rec[char]:
                return 'The string is not balanced.'
        else:
            raise ValueError('The sting must have parentheses, braces, or curly brackets.')
    else:
        return 'The string is balanced.'


print(checkBalance('((([[[]]]{{}}()(){}{}[][](()))))'))
print(checkBalance('()()()'))
print(checkBalance('())'))
