class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0
        window_zeros = 0
        while right < len(nums):
            rnum = nums[right]
            right += 1
            
            if rnum == 0:
                window_zeros += 1
            if window_zeros <= 1:
                res = max(right - left, res)

            while window_zeros > 1:
                lnum = nums[left]
                left += 1
                if lnum == 0:
                    window_zeros -= 1
        return res
