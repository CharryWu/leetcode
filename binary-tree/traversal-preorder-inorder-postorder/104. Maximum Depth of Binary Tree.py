# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftmax = 0
        rightmax = 0
        if root.left:
            leftmax = self.maxDepth(root.left)
        if root.right:
            rightmax = self.maxDepth(root.right)
        
        return max(leftmax, rightmax) + 1
