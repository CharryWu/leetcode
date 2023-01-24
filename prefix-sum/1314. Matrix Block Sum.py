class MatrixSum:
    def __init__(self, mat):
        m, n = len(mat), len(mat[0])
        self.pre = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.pre[i][j] = self.pre[i-1][j] + self.pre[i][j-1] + mat[i-1][j-1] - self.pre[i-1][j-1]
    def getMatrixSum(self, x1, y1, x2, y2):
        return self.pre[x1+1][y1+1] - self.pre[x1+1][y2] - self.pre[x2][y1+1] + self.pre[x2][y2]

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ms = MatrixSum(mat)
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                x1, y1 = min(i + k, m-1) , min(j + k, n-1)
                x2, y2 = max(i-k, 0), max(j-k, 0)
                res[i][j] = ms.getMatrixSum(x1, y1, x2, y2)
        return res
                