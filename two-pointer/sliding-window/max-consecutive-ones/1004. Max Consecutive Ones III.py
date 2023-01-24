class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Translation:
        Find the longest subarray with at most K zeros.
        """
        n = len(nums)
        left, right = 0, 0
        window_zeros = 0
        res = 0
        while right < len(nums):
            rnum = nums[right]
            right += 1
            
            if rnum == 0:
                window_zeros += 1
            if window_zeros <= k:
                res = max(res, right-left)
            
            while window_zeros > k:
                lnum = nums[left]
                left += 1
                if lnum == 0:
                    window_zeros -= 1
            
        return res
