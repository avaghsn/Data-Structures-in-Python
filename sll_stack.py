class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLLStack:
    def __init__(self):
        self.top = None
        self.len = 0

    def __len__(self):
        return self.len

    def __iter__(self):
        temp = self.top
        while temp:
            yield temp.data
            temp = temp.next

    def is_empty(self):
        return self.top is None

    def top(self):
        if self.is_empty():
            return None
        return self.top.data

    def push(self, data):
        node = StackNode(data)
        if self.is_empty():
            self.top = node
            self.len += 1
        else:
            node.next = self.top
            self.top = node
            self.len += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.len -= 1
            return temp.data

    def clear(self):
        self.top = None
        self.len = 0