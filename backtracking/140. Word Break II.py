class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictLen = list(map(lambda s: len(s), wordDict))
        max_candidate_len, min_candidate_len = max(wordDictLen), min(wordDictLen)
        wordDict = set(wordDict)
        n = len(s)
        if n < min_candidate_len:
            return []

        def dp(i, path, res):
            if i == n: # base case，整个 s 都被拼出来了
                res.append(' '.join(path))
            elif n-i < min_candidate_len:
                return
            else:
                for word in wordDict:
                    if i+len(word) <= n and s[i:i+len(word)] == word:
                        path.append(word)
                        dp(i+len(word), path, res)
                        path.pop()

        res, path = [], []
        dp(0, path, res)
        return res