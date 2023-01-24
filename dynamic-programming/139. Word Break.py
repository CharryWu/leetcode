# 备忘录，-1 代表未计算，0 代表 false，1 代表 true
INITIAL = -1
ANS_FALSE = 0
ANS_TRUE = 1

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)

        dp_table = [INITIAL] * n

        def dp(i):
            """
            定义：返回 s[i..] 是否能够被 wordDict 拼出
            """
            if i == n: # base case，整个 s 都被拼出来了
                return True
            if dp_table[i] != INITIAL: # 防止冗余计算
                return True if dp_table[i] == ANS_TRUE else False
            
            # 遍历所有单词，尝试匹配 s[i..] 的前缀
            for word in wordDict:
                l = len(word)
                if i+l > n:
                    continue
                substr = s[i:i+l]
                if substr != word:
                    continue
                # s[i..] 的前缀被匹配，去尝试拼出 s[i+len..]
                if substr == word and dp(i+l): # s[i..] 可以被拼出
                    dp_table[i] = ANS_TRUE
                    return True
            
            dp_table[i] = ANS_FALSE
            return False # s[i..] 无法被拼出

        return dp(0)
"""
# TLE Solution - 在 s 的视角去比较
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)

        dp_table = [False] * n

        def dp(i):
            if dp_table[i]:
                return True
            if s[i:] in wordDict:
                dp_table[i] = True
                return True
            
            for j in range(i+1, n):
                hasLater = dp(j)
                if hasLater and s[i:j] in wordDict:
                    dp_table[i] = True
                    return True
        return dp(0)
"""