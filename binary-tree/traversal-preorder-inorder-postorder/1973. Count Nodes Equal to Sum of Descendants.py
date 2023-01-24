# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(n):
            nonlocal res
            if not n:
                return 0
            
            left_sum = traverse(n.left)
            right_sum = traverse(n.right)
            
            if left_sum + right_sum == n.val:
                res += 1
            
            return left_sum+right_sum+n.val
    
        traverse(root)
        return res