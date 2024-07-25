class Array:
    def __init__(self, size: int = 0):
        self.size = abs(size)
        self.array = [None] * abs(size)
        self.index = 0

    def __setitem__(self, index, data):
        if int(index) < self.size:
            self.array[int(index)] = data
        else:
            raise IndexError("Index out of range")

    def __getitem__(self, index):
        if abs(index) < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of range")

    def __contains__(self, key):
        for i in self.array:
            if i == key:
                return True, f" Element: {self.array[key]}"
            return False

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in self.array:
            yield i

    def __delitem__(self, index):
        """ deletes and shifts all the elements to the left """
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        self.index -= 1

    def __repr__(self):
        return f"Array:\n{[self.array[i] for i in range(len(self.array))]}"

    def clear(self):
        self.array = [None for i in range(self.size)]

    def get(self):
        return self.array

    def add(self, data):
        if abs(self.index) < self.size:
            self.array[self.index] = data
            self.index += 1
        else:
            raise IndexError("Index out of range")

    def resize(self, new_size):
        new_arr = [None] * new_size
        for i in range(len(self.array)):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.size = new_size
        if self.index >= new_size:
            self.index = new_size - 1

    def insert(self, index, data):
        """ inserts at a specified index, shifting subsequent elements to the right """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.index >= self.size:
            self.resize(self.size * 2 if self.size > 0 else 1)
        for i in range(self.size - 1, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = data
        self.index += 1

    def remove(self, data):
        """ removes the first occurrence of a specific element, shifting subsequent elements to the left """
        for i in range(self.size):
            if self.array[i] == data:
                self.__delitem__(i)
                return
        raise ValueError("Element not found in array")

    def pop(self):
        """ removes and returns the last element of the array """
        if self.index == 0:
            raise IndexError("Pop from empty array")
        data = self.array[self.index - 1]
        self.array[self.index - 1] = None
        self.index -= 1
        return data

    def reverse(self):
        left = 0
        right = len(self.array) - 1
        while left < right:
            self.array[left], self.array[right] = self.array[right], self.array[left]
            left += 1
            right -= 1

    def count(self, data):
        """ counts the occurrences of a specific element """
        count = 0
        for i in self.array:
            if i == data:
                count += 1
        return count
