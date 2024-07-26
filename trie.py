from tool_box.array import Array  # import Array from array.py
from tool_box.sll_queue import Queue  # import Queue from sll_queue.py


class TrieNode:
    def __init__(self):
        self.children = Array(26)  # 'a' = 0, 'b' = 1, ..., 'z' = 25
        self.is_end_of_word = False

    def char_to_index(self, char):
        return ord(char) - ord('a')


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr_node = self.root
        for char in word:
            index = curr_node.char_to_index(char)
            if curr_node.children[index] is None:
                curr_node.children[index] = TrieNode()
            curr_node = curr_node.children[index]
        curr_node.is_end_of_word = True

    def search(self, word):
        curr_node = self.root
        for char in word:
            index = curr_node.char_to_index(char)
            if curr_node.children[index] is None:
                return False
            curr_node = curr_node.children[index]
        return curr_node.is_end_of_word

    def starts_with(self, word):
        """ checks if there is any word in the trie that starts with the given prefix """
        curr_node = self.root
        for char in word:
            index = curr_node.char_to_index(char)
            if curr_node.children[index] is None:
                return False
            curr_node = curr_node.children[index]
        return True

    def print(self, curr_node=None, word=""):
        if curr_node is None:
            curr_node = self.root

        if curr_node.is_end_of_word:
            print(" -", word)

        for i in range(26):
            child_node = curr_node.children[i]
            if child_node is not None:
                self.print(child_node, word + chr(i + ord('a')))

    def get_all_words(self, curr_node=None, prefix="", words=None):
        if words is None:
            words = Queue()

        if curr_node is None:
            curr_node = self.root

        if curr_node.is_end_of_word:
            words.enqueue(prefix)

        for i in range(26):
            child_node = curr_node.children[i]
            if child_node is not None:
                self.get_all_words(child_node, prefix + chr(i + ord('a')), words)

        return words
