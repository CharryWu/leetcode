"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def traverse(node, depth):
            if not node:
                return
            if depth >= len(res):
                res.append([])
            res[depth].append(node.val)
            for child in node.children:
                traverse(child, depth+1)
        
        traverse(root, 0)
        return res