def lps(s):
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

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        The idea is to find the longest palindromic subsequence(lps) of the given string.
        |lps - original string| <= k,
        then the string is k-palindrome.

        longest palindromic subsequence:
        LCS of the given string & its reverse will be the longest palindromic sequence.
        """
        n = len(s)

        reversed_str = s[::-1]
        ll = lps(s)

        return (n - ll <= k)
