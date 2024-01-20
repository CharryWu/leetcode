
from collections import deque
DIRS = {(1,0),(0,1),(0,-1),(-1,0)}
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        minutes = 0
        fresh_count = 0
        rotten = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        # print(rotten, fresh_count)
        while len(rotten) > 0 and fresh_count > 0:
            minutes += 1
            for _ in range(len(rotten)):
                topx, topy = rotten.popleft()
                visited.add((topx, topy))
                for dx, dy in DIRS:
                    nx, ny = topx + dx, topy + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        rotten.append((nx, ny))
        return minutes if fresh_count == 0 else -1