class Solution:
    def __init__(self):
        # For storing already solved problems
        self.mp = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        # If both strings are not equal in size
        if len(s2) != n:
            return False

        # If both strings are equal
        if s1 == s2:
            return True

        # If code is reached to this condition then following this are sure:
        # 1. Size of both strings is equal
        # 2. Strings are not equal
        # So size is equal (where size==1) and they are not equal then obviously false
        # Example 'a' and 'b' size is equal, strings are not equal
        if n == 1:
            return False

        key = s1 + " " + s2

        # Check if this problem has already been solved
        if key in self.mp:
            return self.mp[key]

        # For every iteration, it can be in two conditions:
        # 1. We should proceed without swapping
        # 2. We should swap before looking next
        for i in range(1, n):
            # Ex of without swap: gr|eat and rg|eat
            withoutswap = (
                # Left part of the first and second string
                self.isScramble(s1[:i], s2[:i])
                and
                # Right part of the first and second string
                self.isScramble(s1[i:], s2[i:])
            )

            # If without swap gives us the right answer, then we do not need
            # to call the recursion with swap
            if withoutswap:
                self.mp[key] = True
                return True

            # Ex of with swap: gr|eat rge|at
            # Here we compare "gr" with "at" and "eat" with "rge"
            withswap = (
                # Left part of first and right part of second
                self.isScramble(s1[:i], s2[n - i:])
                and
                # Right part of first and left part of second
                self.isScramble(s1[i:], s2[:n - i])
            )

            # If with swap gives us the right answer, then we return True
            # Otherwise, the for loop continues its work
            if withswap:
                self.mp[key] = True
                return True

            # We are not returning False in the else case
            # Because we want to check further cases with the for loop

        self.mp[key] = False
        return False
