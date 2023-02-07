class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        b = [['.'] * n for _ in range(n)]

        def isValid(board, row, col):
                # 检查列是否有皇后互相冲突
                for i in range(row+1):
                    if board[i][col] == 'Q':
                        return False

                # 检查左上方是否有皇后互相冲突
                i, j = row-1, col-1
                while i >= 0 and j >= 0:
                        if (board[i][j] == 'Q'):
                            return False
                        i -= 1
                        j -= 1

                # 检查右上方是否有皇后互相冲突
                i, j = row-1, col+1
                while i >= 0 and j < n:
                        if (board[i][j] == 'Q'):
                            return False
                        i -= 1
                        j += 1

                return True


        def backtrack(board, row):
            if row == n:
                res.append(
                    [''.join(r) for r in board]
                )
                return
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                # print(row, col, n)
                board[row][col] = 'Q' # 做选择
                backtrack(board, row + 1) # 进入下一行决策
                board[row][col] = '.' # 撤销选择

        backtrack(b, 0)
        return res