class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        res = [[0] * m for _ in range(n)]

        # res = transpose(box)
        for i in range(m):
            for j in range(n):
                res[j][i] = box[i][j]
        # flipHorizontal(res)
        for i in range(n):
            for j in range(m//2):
                res[i][j], res[i][m-j-1] = res[i][m-j-1], res[i][j]
        # use two pointer method to move stones to bottom
        for jj in range(m):
            slow = n-1
            for fast in range(n-1, -1, -1):
                if res[fast][jj] == '*':
                    slow = fast - 1
                if res[fast][jj] == '#':
                    res[fast][jj] = '.'
                    res[slow][jj] = '#'
                    slow -= 1
        return res
