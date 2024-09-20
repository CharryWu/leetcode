MOD = 10**9 + 7

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        Let's say we have n elements in our permutation then
        Depending on where we put the element (n+1) in our permutation,
        we may add 0, 1, 2, ..., n new inverse pairs.

        For example, if we have some permutation of 1...4, then:

        5 x x x x creates 4 new inverse pairs
        x 5 x x x creates 3 new inverse pairs
        ...
        x x x x 5 creates 0 new inverse pairs

        if we put n as the last number then all the k inverse pair should come from the first n-1 numbers
        if we put n as the second last number then there's 1 inverse pair involves n so the rest k-1 comes from the first n-1 numbers
        ...
        if we put n as the first number then there's n-1 inverse pairs involve n so the rest k-(n-1) comes from the first n-1 numbers

        DP relation: dp[i][j] = dp[i - 1][j - 0] + dp[i - 1][j - 1] + ... + dp[i - 1][j - (i - 1)]

        It's possible that some where in the right hand side the second array index become negative,
        since we cannot generate negative inverse pairs we just treat them as 0,
        but still leave the item there as a place holder.

        dp[n][k+1] = dp[n-1][k+1]+dp[n-1][k]+dp[n-1][k-1]+dp[n-1][k-2]+...+dp[n-1][k+1-n+1]

        so by deducting the first line from the second line, we have
        dp[n][k+1] = dp[n][k]+dp[n-1][k+1]-dp[n-1][k+1-n]
        """
        # Initialize a DP table, dp[i][j] is the number of arrays of size i with j inverse pairs
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case: 1 way to form 0 inverse pairs with 0 elements

        for size in range(1, n + 1):
            for pairs in range(k + 1):
                # Precondition: dp[size][pairs] = 0
                # dp[n][k+1] = (dp[n][k] + dp[n-1][k+1] - dp[n-1][k+1-n]) % MOD
                dp[size][pairs] += dp[size - 1][pairs]
                dp[size][pairs] += (dp[size][pairs - 1] if pairs > 0 else 0)
                dp[size][pairs] -= (dp[size - 1][pairs - size] if pairs >= size else 0)
                dp[size][pairs] %= MOD

        return dp[n][k]
