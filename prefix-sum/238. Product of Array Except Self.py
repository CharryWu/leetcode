class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftprod = [1] * n
        rightprod = [1] * n

        for i in range(1, n):
            leftprod[i] = leftprod[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            rightprod[i] = rightprod[i+1] * nums[i+1]

        res = [0] * n
        for i in range(n):
            res[i] = leftprod[i] * rightprod[i]
        return res

"""
# 空间复杂度优化过后的解法，不需要 prefix 和 suffix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res
"""
