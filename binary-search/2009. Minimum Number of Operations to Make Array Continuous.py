from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))  # Make `nums` as unique numbers and sort `nums`.
        res = n
        for i, num in enumerate(nums):
            end = num+n-1 # We expect elements of continuous array must in range [start..end]
            window_right_idx = bisect_right(nums, end) # Find right insert position
            res = min(res, n - (window_right_idx-i)) # window_right_idx-i is the count of unique numbers in [start..end] range from nums
            # The cost to make coninuous array is cost = n - uniqueLen
        return res
