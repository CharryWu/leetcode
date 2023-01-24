class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        up, left, right, bottom = 0, 0, n-1, n-1
        k = 1
        
        while k <= n*n:
            if up <= bottom:
                for j in range(left, right+1):
                    res[up][j] = k
                    k += 1
                up += 1
            if left <= right:
                for i in range(up, bottom+1):
                    res[i][right] = k
                    k += 1
                right -= 1
            
            if up <= bottom:
                for j in range(right, left-1, -1):
                    res[bottom][j] = k
                    k += 1
                
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, up-1, -1):
                    res[i][left] = k
                    k += 1
                
                left += 1
        
        return res