from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        numodd = 0
        for key, val in c.items():
            if val % 2 == 1:
                numodd += 1
        return numodd <= 1