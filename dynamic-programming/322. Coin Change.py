class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            if amount in memo:
                return memo[amount]
            min_coin = float('inf')
            for coin in coins:
                prev = dfs(amount - coin)
                if prev == -1:
                    continue

                min_coin = min(min_coin, prev + 1)
            res = -1 if min_coin == float('inf') else min_coin
            memo[amount] = res
            return res
        
        return dfs(amount)

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for val in range(1, amount+1):
            for coin in coins:
                if val - coin >= 0: # 注意要检查 val-coin 是否为负数
                    dp[val] = min(dp[val], dp[val-coin] + 1) # 如果不存在，则dp[val] 一定为 float('inf')，没有一个valid 整数去update 当前的 dp[val]
                
        return dp[amount] if dp[amount] != float('inf') else -1
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1) # 将数组初始化为 amount+1 而不是 INT_MAX，因为之后的 dp[i-coin] + 1 操作会让整数溢出。
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0: # 注意要检查 val-coin 是否为负数
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return -1 if dp[-1] == amount+1 else dp[-1]