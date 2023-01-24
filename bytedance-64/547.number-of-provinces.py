class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        if not n:
            return 0
        visited = [False] * n
        def dfs(u):
            for v in range(n):
                if isConnected[u][v] == 1 and visited[v] == False:
                    visited[v] = True
                    dfs(v)
        count = 0
        for i in range(n):
            if visited[i] == False:
                count += 1
                visited[i] = True
                dfs(i)
        return count





class UnionFind(object):
    def __init__(self, n):
        self.u = list(range(n))
        
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb: self.u[ra] = rb
    
    def find(self, a):
        while self.u[a] != a: a = self.u[a]
        return a
class Solution:
    def findCircleNum(self, isConnected) -> int:
        """
        Union 解法核心：
        将所有有 edge 链接的地方 union 起来，然后再 union 里面 find 寻找有多少 unique item
        """
        s = len(isConnected)
        if not s:
            return 0

        uf = UnionFind(s)
        for r in range(s):
            for c in range(r,s):
                if isConnected[r][c] == 1:
                    uf.union(r,c)

        return len(set([uf.find(i) for i in range(s)]))