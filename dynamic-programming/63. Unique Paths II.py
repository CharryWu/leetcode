class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # edge case: either start or end is blocked
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    dp[i][j] = 1 # base case: # dp[1][1] = 1
                else:
                    if obstacleGrid[i-1][j-1] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]