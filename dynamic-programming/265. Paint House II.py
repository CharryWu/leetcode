class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        dp = [[float('inf')]*k for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            for j in range(k):
                for jj in range(k):
                    if jj == j: # 避免相同的颜色
                        continue
                    dp[i][j] = min(dp[i][j], dp[i-1][jj] + costs[i][j])

        return min(dp[n-1])