class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Let's put all this together into a 2-pass algorithm.
        1. Identify all indexes that should be removed.
        2. Build a new string with removed indexes.

        If we put the indexes of the "(" on the stack,
        then we'll know that all the indexes on the stack at the end
        are the indexes of the unmatched "(".
        We should also use a set to keep track of the unmatched ")" we come across.
        Then, we can remove the character at each of those indexes and then return the edited string.
        """
        stack = []
        indexes_to_remove = set()
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            else:
                if len(stack) == 0: # unmatched ")"
                    indexes_to_remove.add(i)
                else: # matched ")", remove from stack
                    stack.pop()

        indexes_to_remove = indexes_to_remove.union(set(stack))
        res = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                res.append(c)
        return ''.join(res)
