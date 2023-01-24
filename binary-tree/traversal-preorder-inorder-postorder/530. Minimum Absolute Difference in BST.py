# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        
        def traverse(n):
            nonlocal res
            if not n:
                return
            # find left closest value
            if n.left:
                cur = n.left
                while cur:
                    res = min(res, abs(n.val-cur.val))
                    cur = cur.right
                traverse(n.left)

            # find right closest value
            if n.right:
                cur = n.right
                while cur:
                    res = min(res, abs(n.val-cur.val))
                    cur = cur.left
                traverse(n.right)
        
        traverse(root)
        return res