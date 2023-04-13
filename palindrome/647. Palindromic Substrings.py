class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(2*n-1):
            lo, hi = i // 2, (i+1) // 2
            while 0 <= lo <= hi < n and s[lo] == s[hi]:
                count += 1
                lo -= 1
                hi += 1
        return count