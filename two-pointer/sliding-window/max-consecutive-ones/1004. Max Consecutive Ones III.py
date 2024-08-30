class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        zero_count = 0
        i = 0
        for j, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                # k can be zero, the sliding window could be not tolerating any zero,
                # so the sliding window can be empty, condition check must be i <= j to allow empty window
                while zero_count > k and i <= j:
                    if nums[i] == 0:
                        zero_count -= 1
                    i += 1
            res = max(res, j-i+1)
        return res
