INITIAL = -1
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        我们的原问题是求 s[0..] 中不同子序列 t[0..]，可以先看看 s[0] 是否能匹配 t[0]，如果不可以，那没得说，原问题就转化为让 s[1..] 去匹配 t[0..]；
        但如果 s[0] 可以匹配 t[0]，那么又有两种情况，这两种情况是累加的关系：
        1、让 s[0] 匹配 t[0]，那么原问题转化为让 s[1..] 去匹配 t[1..]。
        2、不让 s[0] 匹配 t[0]，那么原问题转化为让 s[1..] 去匹配 t[0..]。
        比如 s = "aab", t = "ab"，就有两种匹配方式：a_b 和 _ab。
        """
        m, n = len(s), len(t)
        memo = [[INITIAL] * n for _ in range(m)]

        def dp(s, i, t, j):
            if j == n: # 子序列全部匹配完成
                return 1
            if n-j > m-i: # 待匹配子序列的长度不应该比字符串的长度还要短
                return 0
            
            if memo[i][j] != INITIAL: # 已经计算过对应状态
                return memo[i][j]

            res = 0 # 状态转移方程
            if s[i] == t[j]:
                res += dp(s, i+1, t, j+1) + dp(s, i+1, t, j)
            else: # s[i]和t[j]不匹配，继续下一个配位符
                res += dp(s, i+1, t, j)
            memo[i][j] = res
            return res
        
        return dp(s, 0, t, 0)