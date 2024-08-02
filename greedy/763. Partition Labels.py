class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # two pass: one pass to build hashmap of char -> lastindex
        # iterate thru s, for each char c, compare last index of char c to current window end pos
        # if pos of last char c is further than current window end pos, update window end pos
        lastIndexMap = {} # character c -> last occured index of c in s
        for i, c in enumerate(s):
            lastIndexMap[c] = i

        curlen = 0
        curend = 0

        res = []
        for i, c in enumerate(s):
            curend = max(curend, lastIndexMap[c])
            curlen += 1

            if curend == i:
                res.append(curlen)
                curlen = 0

        return res
