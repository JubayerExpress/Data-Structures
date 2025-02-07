class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity  # To simulate a stack with limited capacity

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, item):
        if self.is_full():
            raise Exception("Stack Overflow")
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

# Usage example:
s = Stack(3)
s.push(1)
s.push(2)
s.push(3)

print(s.pop())  # Output: 3
print(s.peek())  # Output: 2
print(s.size())  # Output: 2

# Trying to push more than capacity:
# s.push(4) -> Raises Stack Overflow Exception
