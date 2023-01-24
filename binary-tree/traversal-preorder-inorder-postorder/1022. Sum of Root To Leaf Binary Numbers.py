# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(n, cur):
            nonlocal res
            next_cur = cur * 2 + n.val
            if not n.left and not n.right:
                res += next_cur
                return
            if n.left:
                traverse(n.left, next_cur)
            if n.right:
                traverse(n.right, next_cur)
            
            return
        
        if root:
            traverse(root, 0)
        return res
