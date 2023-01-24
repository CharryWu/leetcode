class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[float('inf')]*3 for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            for j in range(3):
                for k in range(3):
                    if j == k: # 避免相同的颜色
                        continue
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + costs[i][j])
        
        return min(dp[n-1])