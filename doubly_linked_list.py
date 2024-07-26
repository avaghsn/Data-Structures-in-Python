class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def delete_pointers(self):
        self.next = None
        self.previous = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __str__(self):
        return " <-> ".join(str(node.data) for node in self.traverse())

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.len

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add_first(self, data):
        node = DLLNode(data)
        if self.is_empty():
            self.tail = self.head = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        self.len += 1

    def add_last(self, data):
        node = DLLNode(data)
        if self.is_empty():
            self.tail = self.head = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.len += 1

    def add_after(self, target_node_data, new_data):
        """ inserts after the target data """
        temp = self.head
        while temp:
            if temp.data == target_node_data:
                new_node = DLLNode(new_data)
                new_node.next = temp.next
                new_node.previous = temp
                if temp.next:
                    temp.next.previous = new_node
                temp.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                self.len += 1
                return
            temp = temp.next
        raise ValueError(f"Node not found")

    def delete_first(self):
        if self.is_empty():
            raise Exception("list is empty")
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        self.len -= 1
        temp.delete_pointers()

    def delete_last(self):
        if self.is_empty():
            raise Exception("list is empty")
        temp = self.tail
        self.tail = self.tail.previous
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.len -= 1
        temp.delete_pointers()

    def delete_this(self, node):
        if node is self.head:
            self.delete_first()
            return
        if node is self.tail:
            self.delete_last()
            return
        if node.previous:
            node.previous.next = node.next
        if node.next:
            node.next.previous = node.previous
        self.len -= 1
        node.delete_pointers()

    def traverse(self):
        if self.is_empty():
            raise Exception("list is empty")
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def traverse_reverse(self):
        if self.is_empty():
            raise Exception("list is empty")
        temp = self.tail
        while temp:
            while temp:
                yield temp
                temp = temp.previous

    def search(self, data):
        if self.is_empty():
            raise Exception("list is empty")
        temp = self.head
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next

    def clear(self):
        while self.head:
            self.delete_first()
