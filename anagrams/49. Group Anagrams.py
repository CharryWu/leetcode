from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-ord('a')] += 1
            grouped[tuple(freq)].append(s)

        res = []
        for k, v in grouped.items():
            res.append(v)
        return res
