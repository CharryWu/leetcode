from typing import List

from bisect import bisect_left
# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # at least, any characters form a subsequence of length 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

    def lengthOfLISReverseSearch(self, nums: List[int]) -> int:
        """
        Reverse checking for better performance
        """
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i-1,-1,-1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

    def lengthOfLISBinarySearch(self, nums: List[int]) -> int:
        res = [] # we dynamically build the solution
        for x in nums:
            # x is larger than last (largest) element in solution,
            # we just extend the solution to include it
            if len(res) == 0 or res[-1] < x:
                res.append(x)
            else: # x smaller than last (largest) element in solution,
                # eligible to replace one in existing solution 
                idx = bisect_left(res, x)  # Find the index of the first element >= x
                res[idx] = x  # Replace that number with x
        return len(res)