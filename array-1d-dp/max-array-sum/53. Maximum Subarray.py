class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('-inf')
        s = 0
        for num in nums:
            s = num + max(s, 0)
            res = max(res, s)
        
        return res
