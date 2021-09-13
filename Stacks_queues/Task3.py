# Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order. Consider the case in which the element is not
# found - raise ValueError with proper info Message
# Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
# Any other element must remain in the queue respecting their order. Consider the case in which the element is not
# found - raise ValueError with proper info Message
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

    def get_from_stack(self, stack, item):
        if item in stack:
            return item
        else:
            raise ValueError
