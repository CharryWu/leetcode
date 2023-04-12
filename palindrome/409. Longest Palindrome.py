from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s) # freq table
        length = 0
        hasOdd = False
        for char, freq in c.items():
            if freq % 2 != 0:
                hasOdd = True
            # print(char, freq)
            length += (freq // 2) * 2

        return length + (1 if hasOdd else 0)