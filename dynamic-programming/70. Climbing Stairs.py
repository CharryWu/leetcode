class Solution:
    def climbStairs(self, n: int) -> int:
        """
        这题很像 509. 斐波那契数：爬到第 n 级台阶的方法个数等于爬到 n - 1 的方法个数和爬到 n - 2 的方法个数之和。
        """
        memo = [0] * (n+1)
        def dp(remaining):
            """
            Param: It takes remaining steps to reach top
            Return: # ways
            """
            if remaining <= 2:
                return 1
            if memo[remaining] > 0:
                return memo[remaining]
            
            total = dp(remaining-1) + dp(remaining-2)
            memo[remaining] = total
            return total
        return dp(n)