class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        res = 0

        n = len(s)

        i, j = 0, 0
        while j < n:
            while s[j] in charset:
                charset.remove(s[i])
                i += 1
            charset.add(s[j])
            res = max(res, j-i+1)
            j += 1
        return res
