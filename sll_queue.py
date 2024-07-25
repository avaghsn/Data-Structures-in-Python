class QueueNode:
    def __init__(self, data):
        self.next = None
        self.data = data

    def delete_next(self):
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, data):
        node = QueueNode(data)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
        self.length += 1

    def dequeue(self):
        if self.front is None:
            raise Exception("Queue is empty")
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:  # If the queue becomes empty, update rear to None
                self.rear = None
            temp.delete_next()
            self.length -= 1
            return temp.data

    def peek_front(self):
        if self.front is None:
            raise Exception("Queue is empty")
        return self.front.data

    def peek_rear(self):
        if self.rear is None:
            raise Exception("Queue is empty")
        return self.rear.data

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def clear(self):
        while not self.is_empty():
            self.dequeue()

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        current = self.front
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)
