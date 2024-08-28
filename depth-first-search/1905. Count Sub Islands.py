directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        We start by iterating through each cell in grid2.
        Upon encountering an unvisited land cell,
        we initiate a DFS to mark all connected land cells as visited.
        During the traversal, we compare each cell in grid2 with the corresponding cell in grid1.
        If any land cell in grid2 maps to a water cell in grid1, the island is disqualified.
        If the island passes the check, it is counted as a sub-island.
        """
        m, n = len(grid1), len(grid1[0])

        def dfs(x, y):
            """
            Goal: find if grid1[x][y] == 0 and grid2[x][y] == 1, if so, return false
            Because grid2 will not form a sub-island in grid1
            """
            if 0 <= x < m and 0 <= y < n and grid2[x][y] == 1:
                if grid1[x][y] == 0:
                    return False
                grid2[x][y] = 0 # mark visited
                res = True
                for dx, dy in directions: # don't short circuit here, we want to mark all cells of island visited
                    res &= dfs(x + dx, y + dy)
                return res
            else:
                # 1. (x, y) is not in boundary of grid1, return True to not interfere with check
                # 2. grid2[x][y] == 0, return True to indicate that the current cell is not part of an island in grid2.
                return True

        count = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        return count
