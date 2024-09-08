from collections import Counter
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        """
        dp[i][j] stores the LARGEST starting index in s1 of the substring
            where s2 has length i and the window ends at j-1 (s2[:i] is totally included in first j characters s1[:j])

        So dp[i][j] would be:
        if s2[i - 1] == s1[j - 1], this means we could borrow the start index from dp[i - 1][j - 1] to make the current substring valid;
        else, we only need to borrow the start index from dp[i][j - 1] which could either exist or not.

        Finally, go through the last row to find the substring with min length and appears first.
        """
        n, m = len(s1), len(s2)

        # Initialize the DP array, m+1 rows and n+1 columns
        dp = [[-1] * (n + 1) for _ in range(m + 1)] # dp[i][j] stores the LARGEST starting index in s1 of the substring

        # when s2 is empty string, the min window in s1 that includes it is still empty string
        # by definition, dp[i][j] stores largest index of min window that ends at j-1 (or first j chars s[:j])
        # so the min window that includes empty string AND ends at j-1 starts at (s1[j:j] == "")
        for j in range(n + 1):
            dp[0][j] = j # s1[j:j] == "" includes s2[:0] == ""

        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # s1[dp[i-1][j-1]:j-1] includes a valid subsequence of s2[:i-1] && s1[j] == s2[i]
                # => s1[dp[i][j]:j] includes a valid subsequence of s2[:i]
                if s2[i - 1] == s1[j - 1]: # current matching s1[j] == s2[i] belongs to same window as s1[j-1] == s2[i-1]
                    dp[i][j] = dp[i - 1][j - 1]
                else: # if no match, need stricter condition: find s2[:i] in first j-1 characters of s1. The start index is same if found
                    dp[i][j] = dp[i][j - 1]


        # Now find the minimum length window
        start, length = 0, n + 1
        for j in range(1, n + 1):
            if dp[m][j] != -1:
                if j - dp[m][j] < length:
                    start = dp[m][j]
                    length = j - dp[m][j]

        return "" if length == n + 1 else s1[start : start + length]
