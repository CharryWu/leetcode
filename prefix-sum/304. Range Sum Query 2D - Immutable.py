class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n+1) for _ in range(m+1)]
        # self.prefix[i][j] 代表以 matrix[0][0] 为左上角，matrix[i-1][j-1] 为右下角 的矩阵的元素总和
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 难点在于找出这个关系，因为self.prefix[i-1][j] 和self.prefix[i][j-1] 计算了两次 matrix[i-1][j-1] 为右下角 的矩阵的元素总和
                # 所以需要减去 self.prefix[i-1][j-1]
                self.prefix[i][j] = self.prefix[i-1][j] + self.prefix[i][j-1] + matrix[i-1][j-1] - self.prefix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.prefix
        # 注意这里 +1 和不 +1 的时机。需要计算的是包括row1, row2, col1, col2 在内的矩阵和
        return p[row2+1][col2+1] - p[row1][col2+1] - p[row2+1][col1] + p[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)