class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Each position has two decisions, open or close parentheses
        We can only add close parentheses when there's an open parentheses before it

        only add open parenthesis if open < n
        only add closing parenthesis if closed < open
        valid IFF open == closed == n
        """
        res = []
        def backtrack(opencount, closecount, path):
            if opencount > n or closecount > n:
                return
            if opencount == closecount == n:
                res.append(''.join(path))
                return

            # two decisions: place ( or )
            # limitation: cannot place ) if closecount >= opencount
            path.append('(')
            backtrack(opencount+1, closecount, path)
            path.pop()

            if closecount < opencount:
                path.append(')')
                backtrack(opencount, closecount+1, path)
                path.pop()

        backtrack(0, 0, [])
        return res
