class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rotate(matrix: List[List[int]]) -> None:
            """
            Do not return anything, modify matrix in-place instead.
            """
            i, j = 0, 0
            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            left, right = 0, n-1
            while left < right:
                for k in range(n):
                    matrix[k][left], matrix[k][right] = matrix[k][right], matrix[k][left]
                left += 1
                right -= 1

            return matrix
    
        for k in range(4):
            if mat == target:
                return True
            if k < 3:
                rotate(mat)