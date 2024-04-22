from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d1 = defaultdict(set)
        d2 = defaultdict(set)

        for u, v in edges:
            d1[u].add(v)
            d2[v].add(u)

        visited = set()
        def dfs(cur):
            if cur == destination:
                return True
            visited.add(cur)
            for neighbor in d1[cur]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            for neighbor in d2[cur]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)
