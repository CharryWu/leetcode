"""
# 自顶向下的递归改为自底向上的迭代解法（超时）
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('-inf')] * n # dp 数组初始化为最小值
        dp[0] = nums[0]
        # 状态转移
        for i in range(1, n):
            for prev in range(max(0, i-k), i):
                dp[i] = max(dp[i], nums[i] + dp[prev])
        
        return dp[-1]
"""

from collections import deque
class Solution: # 利用单调队列结构消除内层循环（通过）
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window = deque([])
        dp = [float('-inf')] * n # dp 数组初始化为最小值
        dp[0] = nums[0] # base case
        window.append(dp[0])
        for p in range(1, n): # 状态转移
            dp[p] = max(window) + nums[p]
            if len(window) == k: # 维护窗口装着 dp[p-1..p-k]
                window.popleft()
            window.append(dp[p])
        
        return dp[n-1]