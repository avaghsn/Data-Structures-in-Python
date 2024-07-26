class CLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __str__(self):
        if self.is_empty():
            return "list is empty."
        result = []
        current = self.head
        while True:
            result.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(result)

    def __len__(self):
        return self.len

    def __iter__(self):
        temp = self.head
        for _ in range(self.len):
            yield temp.data
            temp = temp.next

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def size(self):
        return self.len

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add_first(self, data):
        node = CLLNode(data)
        if self.is_empty():
            self.head = self.tail = node
            node.next = self.head
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.len += 1

    def add_last(self, data):
        node = CLLNode(data)
        if self.is_empty():
            self.head = self.tail = node
            node.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        self.len += 1

    def add_after(self, target_node_data, new_data):
        if self.is_empty():
            raise ValueError("List is empty")
        temp = self.head
        while temp:
            if temp.data == target_node_data:
                new_node = CLLNode(new_data)
                new_node.next = temp.next
                temp.next = new_node
                if temp is self.tail:
                    self.tail = new_node
                self.len += 1
                return
            temp = temp.next
        raise ValueError(f"Node not found")

    def delete_first(self):
        if self.is_empty():
            raise ValueError("List is empty")
        self.head = self.head.next
        self.tail.next = self.head
        self.len -= 1
        if self.len == 0:
            self.head = self.tail = None

    def delete_last(self):
        if self.is_empty():
            raise ValueError("List is empty")
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.len -= 1
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            self.len -= 1
            if self.len == 0:
                self.head = self.tail = None

    def delete_this(self, data):
        if self.is_empty():
            raise ValueError("List is empty")
        if self.head.data == data:
            self.delete_first()
            return
        temp = self.head
        while temp and temp.data != data:
            temp = temp.next
        if temp.next is None or temp.next == self.head:
            raise ValueError(f"Node not found")
        if temp.next == self.tail:
            self.delete_last()
            return
        temp.next = temp.next.next
        self.len -= 1

    def traverse(self):
        if self.is_empty():
            raise Exception("list is empty")
        temp = self.head
        elements = []
        while True:
            elements.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        return elements

    def search(self, value):
        if self.is_empty():
            raise Exception("list is empty")
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def clear(self):
        self.head = self.tail = None
        self.len = 0
