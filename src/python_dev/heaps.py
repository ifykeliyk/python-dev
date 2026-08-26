class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    def insert(self, key, value):
        self.heap.append((key, value))
        self._sift_up(len(self.heap) - 1)

    def peek_min(self):
        if not self.heap:
            raise IndexError("peek_min from an empty heap")
        return self.heap[0]

    def extract_min(self):
        if not self.heap:
            raise IndexError("extract_min from an empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()

        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._shift_down(0)
        return min_element

    def _heapify(self, elements):
        self.heap = list(elements)
        start_index = (len(self.heap) // 2) - 1
        for i in range(start_index, -1, -1):
            self._shift_down(i)

    def meld(self, other_heap):
        combined_heap = self.heap + other_heap.heap
        self._heapify(combined_heap)

        other_heap.heap = []

    def _parent(self, index):
        return (index - 1) // 2 if index != 0 else None

    def _left(self, index):
        left = 2 * index + 1
        return left if left < len(self.heap) else None

    def _right(self, index):
        right = 2 * index + 2
        return right if right < len(self.heap) else None

    def _sift_up(self, index):
        parent_index = self._parent(index)
        while parent_index is not None and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    def _shift_down(self, index):
        while True:
            smallest = index
            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right is not None and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap._heapify([[10, '10'], [5, '5'], [20, '20'], [3, '3']])
    print(min_heap)

    import heapq
    my_list = [10, 5, 20, 3]
    heapq.heapify(my_list)
    print(my_list)

    print(min_heap.extract_min())
    print(min_heap.extract_min())
    print(min_heap.extract_min())

    print(heapq.heappop(my_list))
    print(heapq.heappop(my_list))
    print(heapq.heappop(my_list))
