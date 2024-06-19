from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mp = defaultdict(list)
        for s in strs:
            # compute the "count" value of each string
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            mp[tuple(count)].append(s)

        for key, ll in mp.items():
            res.append([])
            for word in ll:
                res[-1].append(word)
        return res
