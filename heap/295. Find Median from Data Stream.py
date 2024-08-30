import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = [] # store upper half values
        self.maxheap = [] # store lower half values

    def addNum(self, num: int) -> None:
        if len(self.minheap) > 0 and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        # rebalance
        if len(self.minheap) - len(self.maxheap) > 1:
            upper_low = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -upper_low)
        elif len(self.maxheap) - len(self.minheap) > 1:
            lower_high = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, lower_high)

    def findMedian(self) -> float:
        m, n = len(self.minheap), len(self.maxheap)
        if m == n:
            return (self.minheap[0] - self.maxheap[0]) / 2
        elif m > n:
            return self.minheap[0]
        else:
            return -self.maxheap[0]
