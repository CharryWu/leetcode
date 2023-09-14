from collections import deque
DIR = {(0, 1), (0, -1), (1, 0), (-1, 0)}
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        bfs_queue = deque([])
        m, n = len(grid), len(grid[0])
        startRow, startCol = 0, 0
        endRow, endCol = m-1, n-1

        def is_safeval_valid(grid, starti, startj, dist):
            visited = [[False] * n for i in range(m)]
            queue = deque([(starti, startj)])
            if grid[starti][startj] < dist:
                return False
            visited[0][0] = True

            while queue:
                i, j = queue.popleft()
                if i == endRow and j == endCol:
                    return True
                for dx, dy in DIR:
                    nx, ny = dx + i, dy + j
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        if grid[nx][ny] < dist:
                            continue
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return False

            #### DFS
            # visited[i][j] = True

            # for dx, dy in DIR:
            #     nx, ny = i + dx, j + dy
            #     if grid[i][j] >= safeval and is_safeval_valid(grid, visited, nx, ny, safeval):
            #         return True
            # return False

        # BFS on 2D board to mark each cell's distance from nearest thieve
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs_queue.append((i, j))

        while bfs_queue:
            x, y = bfs_queue.popleft()
            for dx, dy in DIR:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = grid[x][y]+1
                        bfs_queue.append((nx, ny))
                    else:
                        grid[nx][ny] = min(grid[x][y]+1, grid[nx][ny])

        ans = 0 # actual safeness factor, it's not known beforehand, we need to guess it, and verify if the guess is correct
        l, r = 1, min(grid[startRow][startCol], grid[endRow][endCol]) # min possible safeval is 0 (dist 0 from thieve), the one-off val is 1, max is 400 which is entire grid
        while l <= r: # use binary search to facilitate the guess
            mid = (l+r) // 2
            if is_safeval_valid(grid, startRow, startCol, mid):
                ans = max(ans, mid)
                l = mid+1
            else:
                r = mid-1

        return ans-1
