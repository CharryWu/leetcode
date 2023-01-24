# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def traverse(node):
            nonlocal res
            if not node:
                return
            if low <= node.val <= high:
                res += node.val
                traverse(node.left)
                traverse(node.right)
            elif node.val < low:
                traverse(node.right)
            elif node.val > high:
                traverse(node.left)

        traverse(root)
        return res