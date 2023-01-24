class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        up, left, right, bottom = 0, 0, n-1, m-1
        res = []
        i, j = 0, 0
        while len(res) < m*n:
            if up <= bottom:
                for j in range(left, right+1):
                    res.append(matrix[up][j])
                up += 1
            
            if left <= right:
                for i in range(up, bottom+1):
                    res.append(matrix[i][right])
                right -= 1
            
            if up <= bottom:
                for j in range(right, left-1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, up-1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
"""
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)] # TO_RIGHT, TO_DOWN, TO_LEFT, TO_UP
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = [0] * (m*n)
        k = 0
        i, j = 0, 0
        bounds = [0, n-1, m-1, 0] # UP, RIGHT, BOTTOM, LEFT
        cur_dir = 0
        VISITED = -101

        while k < m*n:
            res[k] = matrix[i][j]
            matrix[i][j] = VISITED

            dx, dy = DIR[cur_dir]
            if not (bounds[0] <= i + dx <= bounds[2] and bounds[3] <= j + dy <= bounds[1]): # turn at corner
                cur_dir += 1
                dx, dy = DIR[cur_dir]
            elif matrix[i+dx][j+dy] == VISITED: # already been filled, turn direction
                UP, RIGHT, BOTTOM, LEFT = bounds
                bounds = [UP+1, RIGHT-1, BOTTOM-1, LEFT+1]
                cur_dir = 0
                dx, dy = DIR[cur_dir]
            i += dx
            j += dy
            k += 1
        return res
"""