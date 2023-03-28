from typing import List
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # at least, any characters form a substring of length 1
        for i in range(1,n):
                if nums[i-1] < nums[i]:
                    dp[i] = dp[i-1]+1
                else:
                    pass # dp[i] = 1 unchanged


        return max(dp)
