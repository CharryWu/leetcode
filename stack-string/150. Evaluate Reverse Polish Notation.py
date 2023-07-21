from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token.strip('-').isdigit(): # isdigit doesn't handle negative numbers, need to strip '-' character
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1+operand2)
                elif token == '-':
                    stack.append(operand1-operand2)
                elif token == '*':
                    stack.append(operand1*operand2)
                elif token == '/':
                    stack.append(int(operand1/operand2))

        if len(stack) == 1:
            return stack[0]

        return 0
