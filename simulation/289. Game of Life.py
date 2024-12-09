class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Use 4 values, instead of 2 (0/1), to designate the state after update. This allows us to retain the prev state information so updates of current cell won't affect neighbor cell calculations
        1: live -> live cell (no change)
        -1: live -> dead cell
        check abs(nei) == 1: whether nei cell is previously alive (so update doesn't affect calculating its neighbors' next state)
        0: dead -> dead cell (no change)
        2: dead -> live cell (doens't affect the abs(nei) check)

        After ALL cells have been updated, check if cell is > 0. if > 0, the values are 1, 2, then the post-update cell is alive, otherwise the values are 0, -1, dead
        """
        directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        m, n = len(board), len(board[0])

        for x in range(m):
            for y in range(n):
                live = 0
                for dx, dy in directions: # count live neighbors
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and abs(board[nx][ny]) == 1:
                        live += 1
                if board[x][y] == 1 and (live < 2 or live > 3): # Rule 1 or Rule 3: live -> dead
                    board[x][y] = -1
                if board[x][y] == 0 and live == 3: # Rule 4: dead -> live
                    board[x][y] = 2
                # else: Rule 2 no change: dead -> dead, live -> live

        for x in range(m):
            for y in range(n):
                board[x][y] = 1 if board[x][y] > 0 else 0
        return board
