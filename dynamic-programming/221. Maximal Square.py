class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        当 matrix[i][j] 为 1，且它的左边、上边、左上边都存在正方形时，matrix[i][j] 才能够作为一个更大的正方形的右下角：
        以 matrix[i][j] 为右下角元素的最大的全为 1 正方形矩阵的边长为 dp[i][j]。

        if (matrix[i][j] == 1)
            // 类似「水桶效应」，最大边长取决于边长最短的那个正方形
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1;
        else
            dp[i][j] = 0;
        
        题目最终想要的答案就是最大边长 max(dp[..][..]) 的平方。
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)] # 定义：以 matrix[i][j] 为右下角元素的全为 1 正方形矩阵的最大边长为 dp[i][j]。
        max_side = 0

        # base case，第一行和第一列的正方形边长
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
            max_side = max(max_side, dp[i][0]) # 别忘了在这里也更新最长边长
        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
            max_side = max(max_side, dp[0][j]) # 别忘了在这里也更新最长边长
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ) + 1
                    max_side = max(max_side, dp[i][j])
        
        return max_side ** 2