class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set()
        negdiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(i):
            if i == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return

            for j in range(n):
                if j in col or i-j in negdiag or i+j in posdiag:
                    continue
                col.add(j)
                posdiag.add(i+j)
                negdiag.add(i-j)
                board[i][j] = 'Q'

                backtrack(i+1)

                col.remove(j)
                posdiag.remove(i+j)
                negdiag.remove(i-j)
                board[i][j] = '.'

        backtrack(0)
        return res
