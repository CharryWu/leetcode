class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        count_zeros = 0
        left, right = 0, 0

        while right < n:
            if nums[right] == 0:
                count_zeros += 1
                while count_zeros >= 2:
                    count_zeros -= 1 if nums[left] == 0 else 0
                    left += 1
            res = max(res, right-left)
            right += 1
        return res