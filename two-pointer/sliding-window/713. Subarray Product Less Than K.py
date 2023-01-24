class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left, right = 0, 0
        res = 0
        window_product = 1
        
        while right < len(nums):
            rnum = nums[right]
            right += 1
            
            window_product *= rnum
            
            while window_product >= k:
                lnum = nums[left]
                window_product //= lnum
                left += 1
            res += right-left # 注意这里顺序，要放在最后再更新res
                

        return res
