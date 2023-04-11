INITIAL = -1
TRUE = 1
FALSE = 0
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False
        memo = [[INITIAL] * (n+1) for _ in range(m+1)]

        def dp(i, j):
            k = i+j
            if k == len(s3):
                return True
            if memo[i][j] != INITIAL:
                return True if memo[i][j] == TRUE else False
            res = False

            if i < m and s1[i] == s3[k]:
                res = dp(i+1, j)
            if j < n and s2[j] == s3[k]:
                res = res or dp(i, j+1)

            memo[i][j] = TRUE if res else FALSE

            return res

        return dp(0, 0)