from tool_box.array import Array  # import Array from array.py
import math


class HashNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class DynamicHash:
    """ Open Addressing: Double Hashing """

    def __init__(self):
        self.array = Array()
        self.table_size = 0
        self.useful = 0
        self.deleted_count = 0

    def hash_1(self, key):
        """ m * (a * key % 1) , 'a' is golden ratio , 'm' is table-size """
        a = (math.sqrt(5) - 1) / 2
        n = int(self.table_size * (a * key % 1))
        return n

    def hash_2(self, key):
        n = 2 * int(key % self.table_size) + 1
        return n

    def key_to_int(self, key):
        k = 0
        for char in key:
            k += ord(char)
        return k

    def hash_function(self, key, i):
        key = self.key_to_int(key)
        hash_1 = self.hash_1(key)
        hash_2 = self.hash_2(key)
        m = self.table_size
        return (hash_1 + i * hash_2) % m

    def is_full_threshold(self):
        """ return True if n/m >= full threshold which is 0.75 """
        n = self.useful
        m = self.table_size
        return n / m >= 0.75

    def is_empty_threshold(self):
        """ return True if n/m <= empty threshold which is 0.25 """
        n = self.useful
        m = self.table_size
        return n / m <= 0.25

    def rehashing(self, new_array):
        m = len(self.array)
        for item in self.array:
            if item and item != "deleted":
                for i in range(m):
                    index = self.hash_function(item.key, i)
                    if new_array[index] is None:
                        new_array[index] = item
                        break

        return new_array

    def expand(self):
        m = self.table_size
        if m == 0:
            self.array = Array(1)
            self.table_size = 1
            return None

        if self.is_full_threshold():
            self.table_size *= 2
            new_array = Array(self.table_size)
            self.array = self.rehashing(new_array)

    def insert(self, key, data):
        self.expand()
        m = self.table_size
        array = self.array

        for i in range(m):
            index = self.hash_function(key, i)
            if array[index] is None or array[index] == "deleted":
                array[index] = HashNode(key, data)
                self.useful += 1
                return

    def search(self, key):
        m = self.table_size
        arr = self.array

        for i in range(m):
            index = self.hash_function(key, i)
            item = arr[index]
            if item and item != "deleted":
                if item.key == key:
                    return index
        return None

    def update(self, key, value):
        index = self.search(key)
        if index is not None:
            item = self.array[index]
            item.value = value

    def delete(self, key):
        index = self.search(key)
        if index is not None:
            self.array[index] = "deleted"
            self.useful -= 1
            self.deleted_count += 1
            self.shrink()

    def shrink(self):
        if self.is_empty_threshold():
            self.table_size //= 2
            new_array = Array(self.table_size)
            self.array = self.rehashing(new_array)

    def get_item(self, key):
        index = self.search(key)
        if index is not None:
            item = self.array[index]
            return item.data
        return None

    def __len__(self):
        return self.useful

    def __setitem__(self, key, data):
        self.insert(key=key, data=data)

    def __getitem__(self, key):
        return self.get_item(key)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        index = self.search(key)
        if index is not None:
            return True
        else:
            return False

    def __iter__(self):
        for item in self.array:
            if item and item != "deleted":
                yield item.key
