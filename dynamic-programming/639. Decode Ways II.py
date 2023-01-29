MOD = 10**9+7
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        s[i] 本身可能表示一个字母，这种情况下解码数量为 numDecodings(s[0..i-1])
        s[i] 可能和 s[i - 1] 结合起来表示一个字母，这种情况下解码数量为 numDecodings(s[0..i-2])
        想计算解码方法的总数，可以写出如下状态转移方程：
            numDecodings(s) = numDecodings(s[0:-1]) + numDecodings(s[0:-2])
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * (n+1) # 定义：dp[i] 表示长度为i的 s[0..i-1] 的解码方式数量
        # base case: s 为空
        dp[0] = 1
        if ord('1') <= ord(s[0]) <= ord('9'): # base case: s 只有一个字符的情况
            dp[1] = 1
        elif s[0] == '*':
            dp[1] = 9

        for i in range(2, n+1): # 注意 dp 数组和 s 之间的索引偏移一位
            c, d = s[i-1], s[i-2]
            # case1: both c and d are digits
            if c.isdigit() and d.isdigit(): # ...DC...
                # case 1. s[i] 本身可以作为一个字母
                if c != '0':
                    dp[i] += dp[i-1] % MOD
                # case 2. s[i] 和 s[i - 1] 结合起来表示一个字母
                if d == '1' or d == '2' and ord(c) <= ord('6'):
                    dp[i] += dp[i-2] % MOD
            # case2: c is star, d is digit
            elif c == '*' and d.isdigit(): # ...D*...
                # case 1. s[i] 本身可以作为一个字母
                dp[i] += dp[i-1] * 9 % MOD # * 不能代表 '0'
                # case 2. s[i] 和 s[i - 1] 结合起来表示一个字母
                if d == '1':
                    dp[i] += dp[i-2] * 9 % MOD #  * 不能代表 '0', if c = 1..6, 有 6 个数
                if d == '2':
                    dp[i] += dp[i-2] * 6 % MOD
            # case3: d is star, c is digit
            elif d == '*' and c.isdigit(): # ...*C...
                # case 1. s[i] 本身可以作为一个字母
                if c != '0':
                    dp[i] += dp[i-1] % MOD
                # case 2. s[i] 和 s[i - 1] 结合起来表示一个字母
                dp[i] += dp[i-2] % MOD # if d = 1
                if ord(c) <= ord('6'):
                    dp[i] += dp[i-2] % MOD # if d = 2, c has to be 0..6 to form a two-digit num with d
            # case4: both c and d are stars
            elif c == '*' and d == '*': # ...**...
                # case 1. s[i] 本身可以作为一个字母
                dp[i] += dp[i-1] * 9 % MOD
                # case 2. s[i] 和 s[i - 1] 结合起来表示一个字母
                dp[i] += dp[i-2] * 15 % MOD # 11..19, 21..26 有15个数

            dp[i] %= MOD

        return dp[n]