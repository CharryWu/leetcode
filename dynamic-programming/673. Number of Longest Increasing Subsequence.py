from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # initialize two arrays to store the length of the longest increasing subsequence
        # and the number of such subsequences ending at each index
        dp = [1] * len(nums)
        count = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] <= dp[j]:
                        dp[i] = dp[j] + 1
                        # update the number of subsequences ending at i
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1: # has already updated dp[i]
                        count[i] += count[j]

        # find the length of the longest increasing subsequence
        max_len = max(dp)
        # find the number of subsequences with length equal to the length of the longest increasing subsequence
        return sum([count[i] for i in range(len(nums)) if dp[i] == max_len])
