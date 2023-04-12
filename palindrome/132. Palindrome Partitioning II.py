from functools import lru_cache
class Solution:
    def minCutTLE(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def isPalindrome(i, j):
            """
            Check if s[i:j] is valid palindrome
            Note j could be equal to n
            """
            lo, hi = i, j-1
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        dp = [n-1] * (n+1)
        dp[0] = -1
        for i in range(n+1):
            for j in range(i):
                if isPalindrome(j, i):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def isPalindrome(l, r):  # l, r inclusive
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)

        @lru_cache(None)
        def dp(i):  # s[i..n-1]
            if i == n:
                return 0
            ans = float('inf')
            for j in range(i, n):
                if (isPalindrome(i, j)):
                    ans = min(ans, dp(j+1) + 1)
            return ans

        return dp(0) - 1