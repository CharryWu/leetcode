# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def traverse(node, maxval):
            nonlocal res
            if not node:
                return
            
            if node.val >= maxval:
                res += 1
            maxval = max(maxval, node.val)
            traverse(node.left, maxval)
            traverse(node.right, maxval)
        
        traverse(root, float('-inf'))
        return res