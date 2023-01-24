"""
When we find a row-neighbour that is bigger than the global maximum of a column, it means that the row-neighbour is bigger than all the elements of that column. Thus, the global maximum of the neighbour's column must be bigger than its corresponding row-neighbour in our column.

To put it more formally, consider column j whose global maximum lies in row i

if matrix[i][j + 1] > matrix[i][j] 
then matrix[i][j + 1] is bigger than all elements in column j
thus maximum of column j + 1 is bigger than its row-neighbour in column j
thus, there exists some peak in the right half of the matrix
"""

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        leftCol, rightCol = 0, n-1
        while leftCol <= rightCol:
            midCol = (leftCol+rightCol) // 2
            max_row = 0 # max index of midCol
            for i in range(m):
                if mat[max_row][midCol] < mat[i][midCol]:
                    max_row = i
            
            if (midCol == 0 and mat[max_row][midCol] > mat[max_row][midCol+1]) or \
                (midCol == n-1 and mat[max_row][midCol] > mat[max_row][midCol-1]):
                return (max_row, midCol)
            
            if (mat[max_row][midCol] > mat[max_row][midCol-1]) and \
                (mat[max_row][midCol] > mat[max_row][midCol+1]):
                return (max_row, midCol)

            elif midCol > 0 and mat[max_row][midCol-1] > mat[max_row][midCol]:
                rightCol = midCol-1
            else:
                leftCol = midCol+1
            
        return (-1, -1)