def getNeighbors(x, y):
    return {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            grid[i][j] = '0' # island => water to mark visited

            for nx, ny in getNeighbors(i, j):
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '0':
                    dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
