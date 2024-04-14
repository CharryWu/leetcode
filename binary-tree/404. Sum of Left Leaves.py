# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent):
            if not node:
                return 0
            if not node.left and not node.right:
                if node==parent.left:
                    return node.val
                else: # right leave
                    return 0
            return dfs(node.left, node) + dfs(node.right, node)
        return dfs(root.left, root) + dfs(root.right, root)
