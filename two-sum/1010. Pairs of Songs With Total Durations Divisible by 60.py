from collections import defaultdict
from bisect import bisect_left

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        seen = [0]*60
        for i in range(len(time)):
            time[i] = time[i] % 60

        res = 0
        for i in range(len(time)):
            other = (-time[i]) % 60
            # print(other)
            res += seen[other]
            seen[time[i]] += 1
        return res