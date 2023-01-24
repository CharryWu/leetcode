# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node):
            """
            Return Value: (isBST, Sum, min, max)
            """
            nonlocal res
            if not node:
                return True, 0, float('inf'), float('-inf')
            
            lbst, lsum, lmin, lmax = traverse(node.left)
            rbst, rsum, rmin, rmax = traverse(node.right)
            nodesum = lsum + node.val + rsum
            nodemin = min(lmin, rmin, node.val)
            nodemax = max(lmax, rmax, node.val)
            if not lbst or not rbst:
                return False, nodesum, nodemin, nodemax
            
            if node.left and lmax >= node.val:
                return False, nodesum, nodemin, nodemax
            
            if node.right and rmin <= node.val:
                return False, nodesum, nodemin, nodemax
            
            res = max(res, nodesum)
            return True, nodesum, nodemin, nodemax

        traverse(root)
        return res
