class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        解决两个字符串的动态规划问题，一般都是用两个指针 i, j 分别指向两个字符串的最后，然后一步步往前走，缩小问题的规模。
        对于每对儿字符 word1[i] 和 word2[j]，可以有四种操作：

        if word1[i] == word2[j]:
            啥都别做（skip）
            i, j 同时向前移动
        else:
            三选一：
                插入（insert）
                删除（delete）
                替换（replace）
        那么「状态」就是指针 i, j 的位置，「选择」就是上述的四种操作。

        如果使用自底向上的迭代解法，这样定义 dp 数组：dp[i-1][j-1] 存储 word1[0..i] 和 word2[0..j] 的最小编辑距离。dp 数组索引至少是 0，所以索引会偏移一位。
        然后把上述四种选择用 dp 函数表示出来，就可以得出最后答案了。
        """
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        # base cases
        for i in range(1, m+1):
            dp[i][0] = i
        
        for j in range(1, n+1):
            dp[0][j] = j
        
        # 自底向上求解
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j]+1, # 插入 word1 第i位，最小编辑距离为 word1[i-1] 和 word2[j] 状态时的编辑距离 + 1
                        dp[i][j - 1] + 1, # 删除 word1 第i位，最小编辑距离为 word1[i] 和 word2[j-1] 状态时的编辑距离 + 1
                        dp[i - 1][j - 1] + 1 # 替换 word1 第i位，最小编辑距离为 word1[i-1] 和 word2[j-1] 状态时的编辑距离 + 1
                    )
        return dp[m][n]
