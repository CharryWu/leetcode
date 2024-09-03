from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        cs, ct = Counter(), Counter(t)
        res = ""
        i, j = 0, 0 # left, right pointer to s

        def valid(window, need):
            for c in need.keys():
                if window[c] < need[c]:
                    return False
            return True

        while j < m:
            cs[s[j]] += 1
            j += 1

            while i < j and valid(cs, ct):
                if j-i < len(res) or res == "":
                    res = s[i:j]
                cs[s[i]] -= 1
                i += 1

        return res
