class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
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