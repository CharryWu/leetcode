def matched(l, r):
    if l == '(' and r == ')':
        return True
    if l == '[' and r == ']':
        return True
    if l == '{' and r == '}':
        return True
    return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0: # more closing brackets than open brackets
                    return False
                top = stack.pop()
                if not matched(top, c):
                    return False
        return len(stack) == 0
