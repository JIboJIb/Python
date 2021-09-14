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

     def get_from_stack(self, item):
        if item in self.stack:
            return item
        else:
            raise ValueError(f'Element "{item}" did not search.')


stack = Stack()
for i in range(10):
    stack.push(i)
print(stack.get_from_stack(8))
print(stack.get_from_stack(10))


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        if self.queue:
            return True
        else:
            return False

    def peek(self):
        return self.queue[-1]

    def get_from_queue(self, item):
        if item in self.queue:
            return item
        else:
            raise ValueError(f'Element "{item}" did not search.')


q = Queue()
for char in 'honey':
    q.enqueue(char)
print(q.get_from_queue('h'))
print(q.get_from_queue('a'))
