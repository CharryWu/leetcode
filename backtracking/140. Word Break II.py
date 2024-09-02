class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxlen, minlen = float('-inf'), float('inf')
        words = set(wordDict)
        for word in words:
            minlen = min(minlen, len(word))
            maxlen = max(maxlen, len(word))

        n = len(s)
        if n < minlen:
            return []

        res = []

        def backtrack(i, path):
            if i == n:
                res.append(' '.join(path))
                return
            if i + minlen > n:
                return

            for word in words:
                wordlen = len(word)
                if i + wordlen > n:
                    continue
                if s[i:i+wordlen] == word:
                    path.append(word)
                    backtrack(i+wordlen, path)
                    path.pop()

        backtrack(0, [])
        return res

# Memoized DP solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}

        def backtrack(substr):
            """
            substr: string that is a substring of the original string
            return: list of valid strings that can be formed from s
            """
            if substr not in memo:
                result = []
                for word in words:
                    wordlen = len(word)
                    if substr[:wordlen] == word:
                        # base case: s can be consumed wholly
                        if len(substr) == wordlen:
                            result.append(word)
                        else: # s can be consumed partially
                            for newword in backtrack(substr[wordlen:]):
                                result.append(word + " " + newword)
                memo[substr] = result
            return memo[substr]

        return backtrack(s)
