# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xp, yp = None, None
        xd, yd = -1, -1

        def traverse(node, depth, parent):
            nonlocal xp
            nonlocal yp
            nonlocal xd
            nonlocal yd
            if not node:
                return
            
            if node.val == x:
                xp = parent
                xd = depth
                return
            
            if node.val == y:
                yp = parent
                yd = depth
                return
            
            traverse(node.left, depth+1, node)
            traverse(node.right, depth+1, node)
        
        traverse(root, 0, None)
        return xd == yd and xp != yp