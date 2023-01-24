# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def height(n):
            nonlocal res
            if not res:
                return 0
            if not n:
                return 0
            leftH = height(n.left)
            rightH = height(n.right)
            
            if abs(leftH-rightH) > 1:
                res = False
                
            return max(leftH, rightH) + 1
        height(root)
        return res

