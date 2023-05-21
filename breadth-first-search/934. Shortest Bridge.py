LAND = 1
WATER = 0
I1 = 11
I2 = 10
MAX_DIST = 101

DIR = {(0, 1), (0, -1), (1, 0), (-1, 0)}

from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def neighbors(row, col):
            for nx, ny in DIR:
                nrow, ncol = row + nx, col + ny
                if 0 <= nrow < n and 0 <= ncol < n:
                    yield nrow, ncol

        def dfs(i, j, queue):
            grid[i][j] = -1
            queue.append((i, j))
            for x, y in neighbors(i,j):
                if grid[x][y] == 1:
                    dfs(x, y, queue)

        firsti, firstj = -1, -1
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if found:
                    break
                if grid[i][j] == 1:
                    firsti, firstj = i, j
                    found = True

        step, queue = 0, deque()
        dfs(firsti, firstj, queue)

        while queue:
            queuelen = len(queue)
            for _ in range(queuelen):
                i, j = queue.popleft()
                for x, y in neighbors(i,j):
                    if grid[x][y] == 1:
                        return step
                    elif grid[x][y] == 0:
                        grid[x][y] = -1
                        queue.append((x, y))
            step += 1

        return step


    def shortestBridgeTLE(self, grid: List[List[int]]) -> int:
        n = len(grid)
        perimeter = set()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == LAND:
                    hasWater = False
                    # top
                    if grid[max(0, i-1)][j] == WATER:
                        hasWater = True
                    # right
                    if grid[i][min(n-1, j+1)] == WATER:
                        hasWater = True
                    # bottom
                    if grid[min(n-1, i+1)][j] == WATER:
                        hasWater = True
                    # left
                    if grid[i][max(0, j-1)] == WATER:
                        hasWater = True
                    if hasWater:
                        perimeter.add((i, j))

        def find_island(si, sj, code):
            queue = deque([(si, sj)])
            while len(queue):
                x, y = queue.popleft()
                grid[x][y] = code

                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == LAND:
                        queue.append((nx, ny))

        i1marked = False

        for i in range(n):
            for j in range(n):
                if grid[i][j] == LAND:
                    if not i1marked:
                        find_island(i, j, I1)
                        i1marked = True
                    else:
                        find_island(i, j, I2)

        def bfs(si, sj, this_code, that_code): # return min dist to the otherside
            min_dist = MAX_DIST
            visited = set()
            queue = deque([(si, sj, -1)])
            while len(queue):
                x, y, d = queue.popleft()
                visited.add((x, y))
                if d > 0 and grid[x][y] == that_code:
                    min_dist = min(min_dist, d)
                else:
                    for dx, dy in DIR:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and (grid[nx][ny] == WATER or (nx, ny) in perimeter and grid[nx][ny] == that_code):
                            queue.append((nx, ny, d+1))
            return min_dist

        dist = MAX_DIST
        for (si, sj) in perimeter:
            that_code = I2 if grid[si][sj] == I1 else I1
            dist = min(dist, bfs(si, sj, grid[si][sj], that_code))
        return dist