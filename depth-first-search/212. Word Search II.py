class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

DIR = {(0, -1), (0, 1), (1, 0), (-1, 0)}
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        m, n = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if board[r][c] not in node.children or (r, c) in visited:
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            for (dx, dy) in DIR:
                nx, ny = r+dx, c+dy
                if 0 <= nx < m and 0 <= ny < n:
                    dfs(nx, ny, node, word)
            visited.remove((r, c))

        for r in range(m):
            for c in range(n):
                dfs(r, c, root, "")

        return list(res)
