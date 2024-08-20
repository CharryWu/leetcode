DIR = {(0, 1), (0, -1), (-1, 0), (1, 0)}
VISITED_SENTINEL = '#' # any character that will not appear in word charset
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Time Complexity:  O(m*n*4^k), where “K” is the length of the word. And we are searching for the letter m*n times in the worst case.
        Here 4 in 4^k is because at each level of our decision tree we are making 4 recursive calls which equal 4^k in the worst case.
        Space Complexity: O(K), Where k is the length of the given words.
        """
        m, n = len(board), len(board[0])
        def backtrack(i, j, cur):
            if cur == len(word):
                return True

            if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[cur]:
                return False

            temp = board[i][j]
            board[i][j] = VISITED_SENTINEL

            for dx, dy in DIR:
                nx, ny = i + dx, j + dy
                if backtrack(nx, ny, cur+1):
                    return True
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
