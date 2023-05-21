from collections import deque

def shortestBridge(grid):
    def dfs(i, j, firstIsland):
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
            return
        grid[i][j] = -1 # mark first island -1
        firstIsland.append((i, j)) # add points to first island
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    def expand(bridge):
        """
        BFS expand on all points of first island, and see which point can
        reach second island in fewest steps.
        Once reached second island, return immediately
        """
        steps = 0
        while bridge:
            size = len(bridge)
            for _ in range(size):
                i, j = bridge.popleft()
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if ni < 0 or ni >= n or nj < 0 or nj >= n or grid[ni][nj] == -1:
                        continue # skip first island or visited water
                    if grid[ni][nj] == 1: # reached second island, return immediately
                        return steps
                    grid[ni][nj] = -1 # mark all water visited
                    bridge.append((ni, nj))
            steps += 1

    n = len(grid)
    firstIsland = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Step 1: Identify the first island
    found = False
    for i in range(n):
        if found:
            break
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j, firstIsland)
                found = True
                break

    # Step 2: Build the initial bridge from first island
    bridge = deque(firstIsland)

    # Step 3: Expand the bridge
    return expand(bridge)