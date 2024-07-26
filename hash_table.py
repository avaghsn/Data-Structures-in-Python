from tool_box.array import Array  # import Array from array.py
from tool_box.singly_linked_list import SLL  # import SLL from singly_linked_list.py


class HashNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class HashTable:
    """ Closed Addressing: Separate Chaining """

    def __init__(self, size):
        self.table_size = size
        self.table = Array(size)

    def __setitem__(self, key, data):
        index = self.hash_function(key)
        self.create_sll(index)
        sll = self.table[index]
        sll.add_first(HashNode(key, data))

    def __getitem__(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            sll = self.table[index]
            for i in sll:
                if i.data.key == key:
                    return i.data.data
        raise KeyError("not found")

    def __contains__(self, key):
        index = self.hash_function(key)
        sll = self.table[index]
        for i in sll:
            if i.data.key == key:
                return True
        return False

    def __iter__(self):
        for item in self.table:
            if item is not None:
                for node in item:
                    yield node

    def __delitem__(self, key):
        index = self.hash_function(key)
        sll = self.table[index]
        for node in sll:
            if node.data.key == key:
                del sll[node]

    def __len__(self):
        return self.table_size

    def create_sll(self, index):
        if self.table[index] is None:
            self.table[index] = SLL()

    def key_to_int(self, key):
        # DJB2
        hash_value = 5381
        for char in key:
            hash_value = (hash_value * 33) + ord(char)
        return hash_value

    def hash_function(self, key):
        integer = self.key_to_int(key)
        return integer % self.table_size

    def insert_last(self, key, data):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = HashNode(key, data)
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.data = data
                    return
                current = current.next
