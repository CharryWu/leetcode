# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = root.val
        max_depth = 0
        def traverse(n, cur_depth):
            nonlocal max_depth
            nonlocal res
            if not n:
                return
            traverse(n.left, cur_depth+1)
            if cur_depth > max_depth:
                res = n.val
                max_depth = cur_depth
            traverse(n.right, cur_depth+1)

        traverse(root, 0)
        return res