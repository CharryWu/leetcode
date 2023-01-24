class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left, right = 0, 0
        subsum = 0
        
        
        while right < len(nums):
            rnum = nums[right]
            right += 1
            
            subsum += rnum
            
            while subsum >= target:
                res = min(res, right-left)
                lnum = nums[left]
                subsum -= lnum
                left += 1

        return res if res != float('inf') else 0

