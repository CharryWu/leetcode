class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Brute force, backtracking
        """
        def isValid(board, row, col, c):
            for i in range(9): # check duplicates on same row/col/grid
                if board[i][col] != '.' and board[i][col] == c: return False
                if board[row][i] != '.' and board[row][i] == c: return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3] != '.' and board[3*(row//3)+i//3][3*(col//3)+i%3] == c: return False
            return True

        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '.':
                        for c in range(1, 10):
                            c = str(c)
                            if isValid(board, i, j, c):
                                board[i][j] = c

                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        # Tried all combinations and cannot fulfill
                        return False
            return True

        if not board or not board[0]:
            return
        solve(board)
