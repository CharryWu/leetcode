from collections import deque
DIRS = {(1,1),(1,0),(0,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1)}
# NOTE: This problem will TLE if you set visited when you're popping coords from queue;
# however, if you set visited inside inner for loop (decide to put new coords to queue), the TLE test case will pass
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1]:
            return -1
        queue = deque([(0,0)])
        grid[0][0] = 1
        dist = 1
        while queue:
            sz = len(queue)
            for i in range(sz):
                topx, topy = queue.popleft()
                if topx == n-1 and topy == n-1:
                    return dist
                for dx, dy in DIRS:
                    nextx, nexty = topx+dx, topy+dy
                    if 0 <= nextx < n and 0 <= nexty < n and grid[nextx][nexty] == 0:
                        queue.append((nextx, nexty))
                        grid[nextx][nexty] = 1 # NOTE: set visited when you decide to put new coords, not when you're popping it from queue, otherwise TLE

            dist += 1
        return -1
