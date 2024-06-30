from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Multi-source bfs starting from every room
        """
        m, n = len(grid), len(grid[0])
        visited = set()

        def addRoom(r,c):
            if r < 0 or r == m or c < 0 or c == n:
                return # out of bound
            if (r,c) in visited or grid[r][c] == -1:
                return # invalid room (wall) or visited

            visited.add((r,c))
            q.append((r,c))

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        dist = 0
        while q:
            for k in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                addRoom(i+1, j)
                addRoom(i-1, j)
                addRoom(i, j+1)
                addRoom(i, j-1)
            dist += 1
