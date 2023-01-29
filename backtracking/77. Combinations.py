class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            """
            Diff from permutation: inner loop starts from current position,
            not from begin of array
            """
            if len(path) == k:
                res.append(list(path))
            
            for i in range(start, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()

        
        backtrack(1, [])
        return res