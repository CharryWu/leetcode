class Solution:
    def makeGood(self, s: str) -> str:
        # Use stack to store the visited characters.
        stack = []
        
        def isSameLetter(c1, c2):
            return abs(ord(c) - ord(stack[-1])) == 32
        
        # Iterate over 's'.
        for c in list(s):
            # If the current character make a pair with the last character in the stack,
            # remove both of them. Otherwise, we add the current character to stack.
            if stack and isSameLetter(c, stack[-1]):
                stack.pop()
            else:
                stack.append(c)
        
        # Returns the string concatenated by all characters left in the stack.
        return ''.join(stack)
