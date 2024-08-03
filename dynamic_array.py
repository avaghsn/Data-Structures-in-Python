from tool_box.array import Array


class DynamicArray:
    def __init__(self, size: int = 0):
        self.size = abs(size)
        self.array = Array(size)  # import Array class from array.py
        self.useful_data = 0

    def __setitem__(self, index, data):
        if self.useful_data > abs(index):
            self.array[index] = data
        else:
            raise IndexError("Index out of range")

    def __getitem__(self, index):
        if self.size > abs(index):
            return self.array[index]
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        return self.useful_data

    def __iter__(self):
        for i in range(self.useful_data):
            yield self.array[i]

    def __repr__(self):
        return f"Dynamic Array:\n{[self.array[i] for i in range(self.useful_data)]}"

    def get(self):
        return self.array

    def size(self):
        return self.size

    def extend(self):
        if self.size == 0:
            temp = Array(1)
        else:
            temp = Array(2 * self.size)

        for i in range(self.useful_data):
            temp[i] = self.array[i]
        self.array = temp
        self.size = len(temp)
        temp = None
        del temp

    def append(self, item):
        if self.useful_data == self.size:
            self.extend()
            self.array[self.useful_data] = item
        else:
            self.array[self.useful_data] = item

        self.useful_data += 1
        return None

    def insert(self, index, item):
        """ inserts at a specified index, shifting subsequent elements to the right """
        if index < 0 or index > self.useful_data:
            raise IndexError("Index out of range")
        if self.useful_data == self.size:
            self.extend()
        for i in range(self.useful_data, index, - 1):  # -1: the loop will decrement the index by 1 on each iteration.
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.useful_data += 1

    def remove(self, item):
        """ removes the 1st occurrence of an element, shifting subsequent elements to the left """
        for i in range(self.useful_data):
            if self.array[i] == item:
                for j in range(i, self.useful_data):
                    self.array[j] = self.array[j + 1]
                self.array[self.useful_data - 1] = None
                self.useful_data -= 1
                return
        raise ValueError("item not found in array")

    def index(self, item):
        """ returns the index of the first occurrence of a specific element """
        for i in range(self.useful_data):
            if self.array[i] == item:
                return i
        raise ValueError("item not found in array")

    def clear(self):
        self.array = Array(self.size)
        self.useful_data = 0

    def pop(self):
        if self.useful_data == 0:
            raise IndexError("pop from empty array")
        item = self.array[self.useful_data - 1]
        self.array[self.useful_data - 1] = None
        self.useful_data -= 1
        return item

