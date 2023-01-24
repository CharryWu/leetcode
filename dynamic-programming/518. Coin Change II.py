class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
#         dp = [0] * (amount + 1)
#         dp[0] = 1
        
#         for coin in coins:
#             for x in range(coin, amount + 1):
#                 dp[x] += dp[x - coin]
#         return dp[amount]

        num_coin = len(coins)
        dp = [[0] * (amount+1) for _ in range(num_coin+1)]
        for ii in range(num_coin+1):
            dp[ii][0] = 1

        for coin_i in range(1, num_coin+1):
            coin_val = coins[coin_i-1]
            for amount_i in range(1, amount+1):
                if amount_i - coin_val >= 0:
                    dp[coin_i][amount_i] = dp[coin_i-1][amount_i] + dp[coin_i][amount_i-coin_val]
                else:
                    dp[coin_i][amount_i] = dp[coin_i-1][amount_i]
        return dp[num_coin][amount]

