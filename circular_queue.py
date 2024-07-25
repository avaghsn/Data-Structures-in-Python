class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * abs(size)
        self.size = size
        self.max = self.size
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_full(self):
        return self.count == self.max

    def is_empty(self):
        return self.count == 0

    def enqueue(self, data):
        if self.is_full():
            raise Exception("Queue is full")
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % self.max
            self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            element = self.queue[self.front]
            self.front = (self.front + 1) % self.max
            self.count -= 1
            return element

    def front_element(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[self.front]

    def rear_element(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[(self.rear - 1 + self.max) % self.max]

    def clear(self):
        self.queue = [None] * self.max
        self.front = 0
        self.rear = 0
        self.count = 0

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            front = self.front
            for _ in range(self.count):
                print(self.queue[front], end=" ")
                front = (front + 1) % self.max
            print()