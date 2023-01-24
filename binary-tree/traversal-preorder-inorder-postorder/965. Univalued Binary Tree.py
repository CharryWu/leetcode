# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        def traverse(n, val):
            if not n:
                return True
            if n.val != val:
                return False
            
            left = traverse(n.left, val)
            if not left:
                return False
                
            right = traverse(n.right, val)
            if not right:
                return False

            return True
        
        return traverse(root, root.val)