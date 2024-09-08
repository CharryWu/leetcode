from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = ""
        for char in order:
            res += char * freq[char]
            del freq[char]

        for char, f in freq.items():
            res += char * f
        return res
