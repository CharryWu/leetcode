import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Min heap of size k stores the largest k values
        heap[0] is the kth largest value
        """
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)

        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
