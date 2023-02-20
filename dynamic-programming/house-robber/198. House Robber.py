from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Top-down DP recursion
        """
        n = len(nums)
        @cache
        def recurse(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            return max(
                nums[i]+recurse(i-2),
                recurse(i-1),
            )
        return recurse(n-1)

    def rob2(self, nums: List[int]) -> int:
        """
        Bottom-up DP
        """
        n = len(nums)
        # dp[i] = x 表示：
        # 从第 i 间房子开始抢劫，最多能抢到的钱为 x
        # base case: dp[n] = 0
        dp = [0] * (n+1)
        for i in range(1, n+1):
            cur = nums[i-1]
            prev_sum = dp[i-1]
            prev_prev_sum = dp[i-2] if i >= 2 else 0
            dp[i] = max(prev_sum, cur + prev_prev_sum)
        return dp[n]

    def rob3(self, nums: List[int]) -> int:
        """
        Bottom-up DP
        """
        n = len(nums)
        # dp[i] = x 表示：
        # 从第 i 间房子开始抢劫，最多能抢到的钱为 x
        # base case: dp[n] = 0
        prev_sum = 0
        prev_prev_sum = 0
        cur_sum = 0
        max_sum = 0
        for i in range(0, n):
            cur = nums[i]
            prev_prev_sum = prev_sum
            prev_sum = cur_sum
            cur_sum = max(prev_sum, cur+prev_prev_sum)
            max_sum = max(max_sum, cur_sum)
        return max_sum