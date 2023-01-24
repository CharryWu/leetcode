
# def findBlackPixel(self, picture, N):
#     """
#     :type picture: List[List[str]]
#     :type N: int
#     :rtype: int
#     """
#     count = 0
#     for c in zip(*picture):
#         if c.count('B') != N: continue
#         first_row = picture[c.index('B')]
#         if first_row.count('B') != N: continue
#         if picture.count(first_row) != N: continue
#         count += 1
#     return count*N

class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m, n = len(picture), len(picture[0])
        row_map = {}
        col_count = [0] * n
        
        def scanRow(i):
            row_count = 0
            rstr = ""
            for j in range(n):
                if picture[i][j] == 'B':
                    row_count += 1
                    col_count[j] += 1
            if row_count == target:
                return ''.join(picture[i])
            return ""
        
        for i in range(m):
            key = scanRow(i)
            if key:
                if key in row_map:
                    row_map[key] += 1
                else:
                    row_map[key] = 1
        
        res = 0
        for key in row_map:
            if row_map[key] == target:
                for j in range(n):
                    if key[j] == 'B' and col_count[j] == target:
                        res += target
        return res
