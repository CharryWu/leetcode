"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        n = len(root.children)
        curNode = Node(root.val, [None] * n)
        for i in range(n):
            curNode.children[i] = self.cloneTree(root.children[i])
        return curNode