def aggregate(stack):
    while len(stack) > 1 and type(stack[-2]) == int:
        last = stack.pop()
        stack[-1] += last

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    aggregate(stack)
                    if len(stack) > 1 and stack[-2] == '(':
                        num = stack.pop()
                        stack.pop()
                        stack.append(num*2)
                aggregate(stack)
        return sum(stack)
