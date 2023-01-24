from collections import deque
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        s = deque(list(s))
        
        while len(s)>0:
            c = s.popleft()
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
            
        return ''.join(stack)
        
