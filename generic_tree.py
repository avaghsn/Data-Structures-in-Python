from tool_box.singly_linked_list import SLL


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = SLL()
        self.parent = None

    def __repr__(self, level=0):
        ret = " " * (level * 4) + repr(self.value) + "\n"
        for child in self.children:
            ret += child.data.__repr__(level + 1)
        return ret

    def add_child(self, child_node):
        self.children.add_last(child_node)

    def remove_child(self, child_node):
        self.children.delete(child_node)

    def find(self, value):
        if self.value == value:
            return self
        for child in self.children:
            found = child.data.find(value)
            if found:
                return found
        return None


class GenericTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
        self.current_node = self.root  # points to the node you want to apply function to

    def __repr__(self):
        return repr(self.root)

    def is_empty(self):
        return not self.root

    def add(self, parent_value, child_value):
        parent_node = self.root.find(parent_value)
        if parent_node:
            child_node = TreeNode(child_value)
            parent_node.add_child(child_node)
            child_node.parent = parent_node
        else:
            print(f"Parent node with value {parent_value} not found.")

    def find(self, value):
        return self.root.find(value)

    def traverse(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * (level * 4) + str(node.value))
        for child in node.children:
            self.traverse(child.data, level + 1)

    def delete(self, value):
        node_to_delete = self.root.find(value)
        if node_to_delete:
            if node_to_delete.parent:
                node_to_delete.parent.remove_child(node_to_delete)
            else:
                self.root = None
        else:
            print(f"Node with value {value} not found.")


# tree = GenericTree('root')
# tree.add('root', 'child1')
# tree.add('root', 'child2')
# tree.add('child1', 'child1_1')
# tree.add('child1', 'child1_2')
# tree.add('child2', 'child2_1')
#
# tree.traverse()
#
# tree.delete("child1_1")
#
# tree.traverse()
