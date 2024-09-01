# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#
#
#    def move(self, direction: str) -> bool:
#
#
#    def isTarget(self) -> None:
#
#
OPPOSITE = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
DIRS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

from collections import deque
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        visited = set([(0, 0)])
        target = None

        def dfs(master, x, y):
            nonlocal target
            if master.isTarget():
                target = (x, y)
                return True

            ans = False
            for d, (dx, dy) in DIRS.items():
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and master.canMove(d):
                    master.move(d)
                    visited.add((nx, ny))
                    ans |= dfs(master, nx, ny)
                    master.move(OPPOSITE[d])
            return ans

        if not dfs(master, 0, 0): # assume starting position is (0, 0)
            return -1

        queue = deque([(0, 0, 0)])
        while queue:
            x, y, step = queue.popleft()
            if (x, y) == target:
                return step

            for d, (dx, dy) in DIRS.items():
                nx, ny = x + dx, y + dy
                if (nx, ny) in visited:
                    queue.append((nx, ny, step+1))
                    visited.remove((nx, ny))
        return -1


