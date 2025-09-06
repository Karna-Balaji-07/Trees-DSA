import heapq as heap
from typing import List

class KthLargest:
    def __init__(self, k: int, arr: List[int]):
        self.k = k
        self.heap = arr
        heap.heapify(self.heap)
        while len(self.heap) > k:
            heap.heappop(self.heap)

    def add(self, val: int) -> int:
        heap.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heap.heappop(self.heap)
        return self.heap[0]
