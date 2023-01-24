# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def traverse(node, parentval, grandparentval):
            nonlocal res
            if not node:
                return
            if grandparentval % 2 == 0:
                res += node.val
            traverse(node.left, node.val, parentval)
            traverse(node.right, node.val, parentval)
        
        traverse(root, 1, 1)
        return res