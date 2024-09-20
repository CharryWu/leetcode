class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        dp[i][j]: the longest palindromic subsequence's length of substring(i, j), here i, j represent left, right indexes in the string
        State transition:
        dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
        otherwise, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
        Initialization: dp[i][i] = 1
        """
        dp = [[0] * len(s) for _ in range(len(s))] # left, right

        # Fill the DP table
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1  # Single characters are palindromes of length 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(s) - 1]
