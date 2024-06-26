import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        len(piles) <= h, one hour consumes at most one pile
        Binary search on the interval [1, max(piles)] to determine the minimum
        required rate
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l+r) // 2
            # calculate how many hours does it take to eat all bananas for this rate `mid`,
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid) # round up
            if hours <= h: # satisfies the constraint
                res = min(res, mid)
                r = mid - 1 # try to find an even smaller `mid` rate, set right pointer
            else:
                l = mid + 1 # try to find an even bigger `mid` rate, set left pointer to right
        return res
