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
