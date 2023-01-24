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
        dp = [0] * (n+1) # 定义：dp[i] 表示 s[0..i-1] 的解码方式数量
        dp[0], dp[1] = 1, 0 if s[0] == '0' else 1 # base case: s 为空或者 s 只有一个字符的情况

        for i in range(2, n+1): # 注意 dp 数组和 s 之间的索引偏移一位
            c, d = s[i-1], s[i-2]
            # case 1. s[i] 本身可以作为一个字母
            if ord('1') <= ord(c) <= ord('9'):
                dp[i] += dp[i-1]
            # case 2. s[i] 和 s[i - 1] 结合起来表示一个字母
            if d == '1' or d == '2' and ord(c) <= ord('6'):
                dp[i] += dp[i-2]
        return dp[n]