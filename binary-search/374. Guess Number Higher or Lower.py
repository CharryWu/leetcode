# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo+hi) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g > 0:
                lo = mid+1
            else:
                hi = mid-1
        
        return lo
