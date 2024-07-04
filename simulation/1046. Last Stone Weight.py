import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            first = heapq.heappop(maxheap)
            second = heapq.heappop(maxheap)
            if abs(second) == abs(first):
                if not maxheap:
                    return 0
            else:
                heapq.heappush(maxheap, -abs(abs(second)-abs(first)))

        return -maxheap[0]

