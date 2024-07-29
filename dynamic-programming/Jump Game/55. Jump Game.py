class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1] * n
        dp[n-1] = True

        # memoize
        def dfs(i):
            if i >= n:
                return True

            if dp[i] != -1:
                return dp[i]

            for delta in range(1, nums[i]+1):
                if dfs(i+delta):
                    dp[i+delta] = True
                    return True

            return False
        return dfs(0)
