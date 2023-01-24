class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        res = 1
        count = 1
        for i in range(1, n):
            if ord(s[i]) != ord(s[i-1]) + 1:
                count = 1
            else:
                count += 1
                res = max(res, count)
        return res