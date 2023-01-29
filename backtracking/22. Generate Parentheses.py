class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_count, close_count, path):
            nonlocal res
            if open_count > n or close_count > n or close_count > open_count:
                return
            if len(path) == n * 2: # open_count == close_count == n
                res.append(''.join(path))
            
            path.append('(')
            backtrack(open_count+1, close_count, path)
            path.pop()
            
            path.append(')')
            backtrack(open_count, close_count+1, path)
            path.pop()


        backtrack(0, 0, [])
        return res