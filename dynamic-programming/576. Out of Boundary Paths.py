MOD = 10**9+7
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        res = 0
        def encode(i, j, remain):
            return f"{str(i)},{str(j)},{remain}"

        def dp(i, j, remain):
            if remain < 0:
                return 0
            if i == -1 or j == -1 or i == m or j == n:
                return 1
            elif remain == 0:
                return 0

            code = encode(i, j, remain)
            if code in memo:
                return memo[code]
            cur = dp(i+1, j, remain-1) % MOD + dp(i-1, j, remain-1) % MOD + dp(i, j-1, remain-1) % MOD + dp(i, j+1, remain-1) % MOD
            memo[code] = cur % MOD
            return memo[code]
        
        return dp(startRow, startColumn, maxMove)


