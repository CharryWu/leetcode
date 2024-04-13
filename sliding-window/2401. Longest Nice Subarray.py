class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        i = 0
        n = len(nums)
        ors = 0
        for j in range(n):
            # use while loop to readjust window until it's nice!
            while ors & nums[j] != 0: # pair-wise AND has non-zero results
                ors ^= nums[i]
                i += 1
            ors |= nums[j]
            res = max(res, j-i+1)
        return res
