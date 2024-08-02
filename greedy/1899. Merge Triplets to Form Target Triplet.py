class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 1. go through list of triplets, filter out triples ti, tj, tk that has ti > target[i], tj > target[j], tk > target[k]
        # 2. for each target[i,j,k], check remaining triplets (that have values less than or equal target at corresponding position),
        # if have value exactly equal target[i], target[j], target[k]. If all three positions have match, return true, otherwise false
        checkedPos = [False, False, False]

        for t in triplets:
            ti, tj, tk = t
            if ti > target[0] or tj > target[1] or tk > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    checkedPos[i] = True


        return all(checkedPos)
