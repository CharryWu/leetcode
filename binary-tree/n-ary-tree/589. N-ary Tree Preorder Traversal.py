"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(n):
            res.append(n.val)
            
            for child in n.children:
                if child:
                    dfs(child)
        if root:
            dfs(root)
        return res


"""
from collections import deque
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = deque([root]) # 注意这里是FILO stack，不是FIFO queue。否则就变成层顺遍历了
        while stack:
            n = stack.pop() # 从堆栈顶部pop
            res.append(n.val)
            for child in n.children[::-1]: # 这里需要将子元素反序装入。pop 的时候就变成正序了
                if child:
                    stack.append(child)
        return res
"""
