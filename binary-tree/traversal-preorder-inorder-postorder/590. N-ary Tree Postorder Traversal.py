"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        def dfs(n):
            for child in n.children:
                if child:
                    dfs(child)
            res.append(n.val)
        dfs(root)
        return res


"""
# 用两个stack去实现后缀遍历。最终 stack2 反过来就是所求的后缀
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack1 = [root]
        stack2 = []
        
        while stack1:
            top1 = stack1.pop()
            for child in top1.children:
                if child:
                    stack1.append(child)
            
            stack2.append(top1.val)
        
        return stack2[::-1]
"""


"""

# Definition for a Node.
# class Node:
#    def __init__(self, val=None, children=None):
#        self.val = val
#        self.children = children
# 可以将前缀遍历直接反转得到后续遍历结果，只有一点不同：每层子节点的顺序也必须反过来，所以这里没有用 n.children[::-1]

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        # Iteration is basically pre-order traversal but rather than go left, go right first then reverse its result.

        while stack:
            n = stack.pop()
            res.append(n.val)
            for child in n.children:
                if child:
                    stack.append(child)
        return res[::-1]

"""

