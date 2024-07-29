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


class Solution:

    def countPalindrome(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPalindrome(s, i, i)
            res += self.countPalindrome(s, i, i + 1)
        return res
