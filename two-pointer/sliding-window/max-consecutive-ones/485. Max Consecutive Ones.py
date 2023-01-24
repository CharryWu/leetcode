class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0

        while right < len(nums):
            rnum = nums[right]
            right += 1
            
            if rnum == 1:
                res = max(res, right-left)
            else:
                window_ones = 0
                left = right
        return res
