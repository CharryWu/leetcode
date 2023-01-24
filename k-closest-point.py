import heapq
class Solution:
    def kClosest(self, points, K: int):
        print(points)
        heap = []
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y)) # max-heap 一超出容量总是 pop 掉最大的（负值最小的）导致堆里面只剩下前k小的
            else:
                heapq.heappush(heap, (dist, x, y))
        return [(x,y) for (dist,x, y) in heap]


test1 = [[1, 3], [-2, 2]]
test2 = [[3, 3], [5, -1], [-2, 4]]
# Solution().kClosest(test1, 1)
Solution().kClosest(test2, 2)