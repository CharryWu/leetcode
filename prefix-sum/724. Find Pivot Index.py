class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        postsum = [0] * (n+1)
        prefix = 0
        for i in range(1, n+1):
            prefix += nums[i-1]
            presum[i] = prefix
        
        suffix = 0
        
        for i in range(n-1, -1, -1):
            suffix += nums[i]
            postsum[i] = suffix
        
        
        for i in range(n):
            if presum[i] == postsum[i+1]:
                return i
        
        return -1
