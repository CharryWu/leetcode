# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def traverse(n):
            """
            返回以n开始的子树的最小和最大的数值
            """
            nonlocal res
            
            if not n.left and not n.right:
                return n.val, n.val
            
            lmin, lmax = n.val, n.val
            rmin, rmax = n.val, n.val
            
            if n.left:
                lmin, lmax = traverse(n.left)
            if n.right:
                rmin, rmax = traverse(n.right)
            
            res = max(
                res,
                abs(n.val-lmin),
                abs(n.val-lmax),
                abs(n.val-rmin),
                abs(n.val-rmax),
            )
            
            return min(lmin, rmin, n.val), max(lmax, rmax, n.val)
        
        traverse(root)
        return res
