class Solution:
    def integerBreak(self, n: int) -> int:
        """
        明白动态规划本质上是穷举这道题就简单了，比方说 n = 4，我们可以把 4 拆分成 1 + 3, 2 + 2，对应的乘积就是 1 * 3, 2 * 2。
        但此时我们直接比较 1 * 3, 2 * 2 的大小还不够，因为 3, 2 它们可能还会被分解成 1 * 2, 1 * 1，也就是说把 n = 4 进一步分解成 1 * (1 * 2), 2 * (1 * 1)，这两种可能也要纳入考虑。
        到底需不需要进一步分解呢？不知道，所以我们都穷举一遍取最大值就可以了。
        integerBreak(4) = max(1 * 3, 1 * integerBreak(3), 2 * 2, 2 * integerBreak(2))
        ```
        int res = Integer.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            res = max(res, i * max(integerBreak(n - i), n - i));
        }
        ```
        """
        memo = [-1] * (n+1)
        memo[1] = 1 # base case
        def dp(num: int) -> int:
            if memo[num] != -1:
                return memo[num]
            res = 0
            for i in range(1, num//2+1): # 优化：只用比较到 i=1..num//2 就行了
                res = max(res, i * (num-i), i * dp(num-i))
            memo[num] = res
            return res
        
        return dp(n)
