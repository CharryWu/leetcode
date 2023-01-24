class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        row, col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        
        count = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row[i] == 1 and col[j] == 1:
                    count += 1
                    
        return count
