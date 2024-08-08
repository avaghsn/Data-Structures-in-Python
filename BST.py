from tool_box.sll_queue import Queue


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return not self.root

    def inorder_traversal(self):
        self.inorder(self.root)

    def preorder_traversal(self):
        self.preorder(self.root)

    def postorder_traversal(self):
        self.postorder(self.root)

    def level_order_traversal(self):
        self.level_order(self.root)

    def inorder(self, node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.data, end="  ")
            self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def preorder(self, node):
        if node is None:
            return
        else:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def level_order(self, root):
        queue = Queue()
        queue.enqueue(root)
        while queue.length > 0:
            temp = queue.dequeue()
            print(temp.data, end="  ")
            if temp.left is not None:
                queue.enqueue(temp.left)
            if temp.right is not None:
                queue.enqueue(temp.right)

    def insert(self, data):
        node = BSTNode(data)
        if self.is_empty():
            self.root = node
            return
        temp = self.root
        while temp.data != data:
            if node.data > temp.data:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = node
                    return
            if node.data < temp.data:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = node
                    return

    def delete_value(self, root, key):
        # base case
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete_value(root.left, key)
        elif key > root.data:
            root.right = self.delete_value(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_larger_node = self.find_min(root.right)
            root.data = min_larger_node.data
            root.right = self.delete_value(root.right, min_larger_node.data)

        return root

    def delete(self, data):
        self.root = self.delete_value(self.root, data)

    def search(self, data):
        temp = self.root
        while temp is not None:
            if temp.data == data:
                return temp
            elif temp.data > data:
                temp = temp.left
            else:
                temp = temp.right
        return None

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1
