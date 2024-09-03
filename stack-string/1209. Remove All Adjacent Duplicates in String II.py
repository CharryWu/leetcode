class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue

            # either c belongs to last consecutive k duplicate characters
            # or c is a different character
            if stack[-1][0] == c:
                stack[-1] += c
            else:
                stack.append(c)

            # remove stack[-1] if it is too long
            while stack and len(stack[-1]) >= k:
                top = stack.pop()
                top = top[:len(top)-k]
                if top != "": # has residual after remove k characters, add it back
                    stack.append(top)
                # merge last two strings if equal
                if len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                    stack.append(stack.pop() + stack.pop())
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

