class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            i, j = row, 0
            val = matrix[i][j]
            while i < len(matrix) and j < len(matrix[i]):
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1

        for col in range(1, cols):
            i, j = 0, col
            val = matrix[i][j]
            while i < len(matrix) and j < len(matrix[i]):
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1
        return True
