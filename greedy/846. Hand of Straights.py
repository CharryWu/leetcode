from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        # We use a minheap to store remainingCount, values
        # Each group consumes one count of a value, we want to use value with min freq as much as possible
        # Note that minheap should always start from smallest remaining value, if there's lowest frequency
        # that IS NOT the min value among remainings, then nothing should be notified

        # failed cases:
        # 1. number of items not divisible by groupsize, some items are left behind
        # and not forming a group
        if n % groupSize != 0:
            return False

        # 2. some items cannot form consecutive groups with other values
        # 3.
        freq = Counter(hand)
        heap = []
        for val, count in freq.items():
            heapq.heappush(heap, val)

        while heap:
            first = heap[0]
            for val in range(first, first + groupSize):
                if val not in freq: # case 2: found a hold in group, cannot form group
                    return False
                freq[val] -= 1 # consume val
                if freq[val] == 0:
                    if val != heap[0]: # case 3:
                        return False
                    heapq.heappop(heap)
        return True
