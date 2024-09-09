
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
def solution(firstList, secondList):
    result = []

    i, j = 0, 0

    while i < len(firstList) and j < len(secondList):
        newstart = max(firstList[i][0], secondList[j][0])
        newend = min(firstList[i][1], secondList[j][1])

        if newstart <= newend:
            result.append((newstart, newend))

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return result

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
solution(firstList, secondList)

i = 0, j = 0, (newstart, newend) = (1, 2), result = [(1,2)]. i += 1 = 1
i = 1, j = 0, (newstart, newend) = (5, 5), result = [(1,2), (5, 5)]. j += 1 = 1
i = 1, j = 1, (newstart, newend) = (8, 10), result = [(1,2), (5, 5), (8,10)]. i += 1 = 2
i = 2, j = 1, (newstart, newend) = (13, 12), result = [(1,2), (5, 5), (8,10)]. j += 1 = 2
//
i = 2, j = 2, (newstart, newend) = (13, 12), result = [(1,2), (5, 5), (8,10)]. j += 1 = 2


# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Input: grid = [[0,1],
 #               [1,0]
 #                    ]
# Output: 2


DIR = {(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)}
from collections import deque
def solution(grid):
    n = len(grid)
    if n == 0:
        return -1

    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    queue = deque((0, 0, 1)) # (x, y, dist)
    visited = set([(0,0)]) # (x, y) visited

    while queue:
        x, y, dist = queue.popleft()
        if x == n-1 and y == n-1:
            return dist

        for dx, dy in DIR:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx,ny) not in visited:
                queue.append((nx,ny,dist+1))
                visited.add(nx, ny)
    6
    return -1

solution( [[0,1],
            [1,0]
        ]) # 2

n = 2
queue = [(0,0,1)]

x = 0, y = 0, dist = 1
    - queue = ((1,1,2)), visited = {(1,1)}

x = 1, y = 1, dist = 2
    - return 2
