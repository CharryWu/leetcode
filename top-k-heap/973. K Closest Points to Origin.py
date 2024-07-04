### MIN heap solution
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            heapq.heappush(h, (x*x + y*y, x, y))
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(h)
            res.append((x,y))
        return res


### MAX heap solution
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            if len(maxheap) <= k or dist < -maxheap[0][0]:
                heapq.heappush(maxheap, (-dist, x, y))

            if len(maxheap) > k:
                heapq.heappop(maxheap)

        res = []
        for d, x, y in maxheap:
            res.append((x, y))
        return res
