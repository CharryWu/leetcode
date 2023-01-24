class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res = []
        items1.sort()
        items2.sort()
        p1, p2 = 0, 0

        while p1 < len(items1) and p2 < len(items2):
            v1, w1 = items1[p1]
            v2, w2 = items2[p2]
            if v1 == v2: # merge case
                res.append([v1, w1+w2])
                p1 += 1
                p2 += 1
            elif v1 < v2:
                res.append([v1, w1])
                p1 += 1
            elif v1 > v2:
                res.append([v2, w2])
                p2 += 1
        while p1 < len(items1):
            res.append(items1[p1])
            p1 += 1
        while p2 < len(items2):
            res.append(items2[p2])
            p2 += 1
        return res