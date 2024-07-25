class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def delete_pointers(self):
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def __getitem__(self, item):
        if not 0 <= item < self.len:
            raise IndexError("Index out of bounds")
        for i, node in enumerate(self):
            if i == item:
                return node

    def __delitem__(self, node):
        if node is self.head:
            self.delete_first()
            return
        if node is self.tail:
            self.delete_last()
            return
        for sll_node in self:
            if sll_node.next is node:
                temp = node.next
                sll_node.next = temp
                node.data = None
                node.next = None
                del node
                self.len -= 1
                return

    def __repr__(self):
        return " -> ".join(str(node.data) for node in self)

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def head_node(self):
        if self.is_empty():
            raise Exception("list is empty")
        return self.head

    def add_first(self, data):
        node = SLLNode(data)
        if self.is_empty():
            self.tail = node
        node.next = self.head
        self.head = node
        self.len += 1

    def add_last(self, data):
        node = SLLNode(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.len += 1

    def add_after(self, target_node_data, new_data):
        """ inserts after the given data """
        temp = self.head
        while temp:
            if temp.data == target_node_data:
                new_node = SLLNode(new_data)
                new_node.next = temp.next
                temp.next = new_node
                if new_node.next is None:
                    self.tail = new_data
                self.len += 1
                return
            temp = temp.next
        raise ValueError(f"Node with data {target_node_data} not found")

    def insert(self, index, data):
        if index < 0 or index > self.len:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.add_first(data)
        elif index == self.len:
            self.add_last(data)
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node = SLLNode(data)
            new_node.next = temp.next
            temp.next = new_node
            self.len += 1

    def delete_first(self):
        if self.is_empty():
            raise Exception("list is empty")
        else:
            self.head = self.head.next
            if self.len == 1:
                self.tail = self.head
            self.len -= 1

    def delete_last(self):
        if self.is_empty():
            raise Exception("list is empty")

        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.len -= 1
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.len -= 1

    def delete(self, data):
        if self.is_empty():
            raise Exception("list is empty")

        if self.head.data == data:
            self.delete_first()
            return

        prev = None
        curr = self.head
        while curr and curr.data != data:
            prev = curr
            curr = curr.next
        if curr is None:
            raise ValueError("not found")
        if curr == self.tail:
            self.delete_last()
        else:
            prev.next = curr.next
            self.len -= 1

    def delete_node(self, node):
        self.__delitem__(node)

    def traverse(self):
        if self.is_empty():
            raise Exception("list is empty")
        else:
            temp = self.head
            while temp:
                yield temp
                temp = temp.next

    def search(self, value):
        if self.is_empty():
            raise Exception("list is empty")
        else:
            temp = self.head
            while temp:
                if temp.data == value:
                    return temp.data
                temp = temp.next
            return None

    def clear(self):
        while self.head:
            self.delete_first()

