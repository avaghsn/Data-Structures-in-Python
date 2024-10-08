from tool_box.dynamic_array import DynamicArray  # import DynamicArray from dynamic_array.py


class MinHeap:
    def __init__(self):
        self.heap = DynamicArray()

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            parent_idx = self.parent(index)
            self.heap[parent_idx], self.heap[index] = self.heap[index], self.heap[parent_idx]
            index = parent_idx

    def heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("empty heap")
        min_item = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.useful_data -= 1
        self.heapify_down(0)
        return min_item

    def get_min(self):
        if len(self.heap) == 0:
            raise IndexError("empty heap")
        return self.heap[0]

    def size(self):
        return len(self.heap)
