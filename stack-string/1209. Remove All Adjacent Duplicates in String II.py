from collections import deque
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        s = deque(list(s))
        
        while len(s)>0:
            c = s.popleft()

            # 在出现第k个重复字符时，stack中只有k-1个重复字符，所以我们只用pop k-1次
            if len(stack) >= k-1 and stack[-k+1:] == [c]*(k-1):
                for _ in range(k-1):
                    stack.pop()
            else:
                stack.append(c)
            
        return ''.join(stack)


"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]] # 这里用一个小技巧，将相同字符归纳成 [char, freq] 的 tuple。减少比较的时间
        
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
                
        

        return ''.join([c * no for c, no in stack])
"""
        
