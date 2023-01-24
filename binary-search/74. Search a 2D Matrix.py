class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        upRow, downRow = 0, m-1
        targetRow = -1
        while upRow <= downRow:
            midRow = (upRow+downRow) // 2
            if matrix[midRow][0] == target:
                downRow = midRow-1
            elif target < matrix[midRow][0]:
                downRow = midRow-1
            elif target > matrix[midRow][0]:
                upRow = midRow+1

        targetRow = min(m-1, max(0, upRow))
        if matrix[targetRow][0] > target:
            targetRow -= 1

        leftCol, rightCol = 0, n-1
        while leftCol <= rightCol:
            midCol = (leftCol+rightCol) // 2
            if matrix[targetRow][midCol] == target:
                rightCol = midCol-1
            elif target < matrix[targetRow][midCol]:
                rightCol = midCol-1
            elif target > matrix[targetRow][midCol]:
                leftCol = midCol+1

        if leftCol == n:
            return False
        return matrix[targetRow][leftCol] == target