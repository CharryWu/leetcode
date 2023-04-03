class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # DP Definition: the LCS of s1[0..i-1] and s2[0..j-1] has length dp[i][j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # Target: compute the LCS length of s1[0..m-1] and s2[0..n-1], which is dp[m][n]
        # base case: dp[0][..] = dp[..][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Since i and j start from one, we use their value minus one indexed into string
                if s1[i - 1] == s2[j - 1]:
                    # s1[i-1] and s2[j-1] must exist in lcs
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # At least one of s1[i-1] or s2[j-1] doesn't exist in LCS
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[m][n]