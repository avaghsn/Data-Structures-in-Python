class ArrayStack:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.pointer = -1

    def __iter__(self):
        temp = self.pointer
        while temp >= 0:
            yield self.array[temp]
            temp -= 1

    def __len__(self):
        return self.pointer + 1

    def top(self):
        if self.pointer >= 0:
            return self.array[self.pointer]
        return None

    def push(self, data):
        if self.pointer >= self.size - 1:
            return f"Overflow, can't push {data}."
        else:
            self.pointer += 1
            self.array[self.pointer] = data

    def pop(self):
        if self.pointer >= 0:
            data = self.array[self.pointer]
            self.pointer -= 1
            return data
        raise IndexError("Empty stack")

    def is_empty(self):
        if self.pointer == -1:
            return True
        return False

    def is_full(self):
        if self.pointer == self.size - 1:
            return True
        return False

    def clear(self):
        self.array = [None] * self.size
        self.pointer = -1