class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Each position has two decisions, open or close parentheses
        We can only add close parentheses when there's an open parentheses before it

        only add open parenthesis if open < n
        only add closing parenthesis if closed < open
        valid IFF open == closed == n
        """
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n: # base case: found valid parenthesis
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0, 0)
        return res
