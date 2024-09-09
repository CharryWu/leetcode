from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        2 key observations:
        1. Diagonals are defined by the sum of indicies in a 2 dimensional array
        2. The snake phenomena can be achieved by reversing every other diagonal level, therefore check if divisible by 2
        """
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d[i+j].append(mat[i][j])
        ans = []
        for entry in d.items():
            if entry[0] % 2 == 0:
                ans.extend(entry[1][::-1])
            else:
                ans.extend(entry[1])
        return ans
