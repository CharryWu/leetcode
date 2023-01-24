class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = [1] * n
        prefix = [1] * n # prefix 是不包括 i 的前缀和
        suffix = [1] * n # suffix 是不包括 i 的后缀和
        
        i = 0
        cur = 1
        while i < n:
            prefix[i] = cur
            cur = cur * nums[i]
            i += 1
        
        cur = 1
        i = n-1
        while i >= 0:
            suffix[i] = cur
            cur = cur * nums[i]
            i -= 1
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res

"""
# 空间复杂度优化过后的解法，不需要 prefix 和 suffix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = [1] * n
        
        i = 0
        cur = 1
        while i < n:
            res[i] = cur # 注意这句和下句的顺序不能颠倒。先写入res[i]保证res[i]存的是 i-1 的 running product
            cur = cur * nums[i]
            i += 1
        
        cur = 1
        i = n-1
        while i >= 0:
            res[i] = res[i] * cur
            cur = cur * nums[i]
            i -= 1
        
        return res
"""
