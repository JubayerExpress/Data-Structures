class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1  # Reset queue when last item is removed
        else:
            self.front = (self.front + 1) % self.capacity
        return data

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        if self.rear >= self.front:
            print("Queue:", self.queue[self.front:self.rear+1])
        else:
            print("Queue:", self.queue[self.front:] + self.queue[:self.rear+1])

# Test cases
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()  # Output: [10, 20, 30]
cq.dequeue()
cq.display()  # Output: [20, 30]

