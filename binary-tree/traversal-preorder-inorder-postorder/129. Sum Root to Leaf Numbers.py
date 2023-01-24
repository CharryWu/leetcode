# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def traverse(n, path):
            nonlocal res
            if not n:
                return
            
            new_path = path*10 + n.val
            if not n.left and not n.right:
                res += new_path
            
            traverse(n.left, new_path)
            traverse(n.right, new_path)
            
        traverse(root, 0)
        return res