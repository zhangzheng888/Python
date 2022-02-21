"""
Stacks

Stack is a LIFO (last-in, first-out) data structure

Typically functions include:
- Push (Append in python)
- Pop

For Python, stacks are generated using lists

Use append() to push an item onto the stack
Use pop() to remove an item


"""

"""
Constructor

stack =  list() or []

stack.append(10)
stack.append(20)

stack.pop()

"""

"""
Stack using List with a wrapper class

Stack class with full set of stack methods

The underlying data structure is a Python list

For pop and peek methods, the stack is checked for empty first to avoid
exceptions
"""

class Stack():

    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self:
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)
