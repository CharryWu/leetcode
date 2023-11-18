from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sliding window, j is the new element to consider
        nums.sort() # sort so that elements closest but smaller to j will be on the left side of j, turning this problem into sliding window problem
        n = len(nums)
        i = 0
        s = 0
        res = 0
        for j in range(n):
            s += nums[j]
            potential_sum = nums[j] * (j-i+1) # make all elements inside [i, j] -> nums[j]
            if s + k < potential_sum:
                s -= nums[i]
                i += 1
            else:
                res = max(res, j-i+1)
        return res
