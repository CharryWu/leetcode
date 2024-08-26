# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        globalmax = float('-inf') # globalmax CANNOT be init to 0
        def dfs(node):
            nonlocal globalmax
            if not node:
                return 0
            val = node.val
            leftmax = max(dfs(node.left), 0) # discard left tree if it's negative
            rightmax = max(dfs(node.right), 0) # discard right tree if it's negative
            globalmax = max(globalmax, leftmax + rightmax + val) # poly-line passing through node, but not going through node's parent
            return val + max(leftmax, rightmax) # single line passing through `node`
        dfs(root)
        return globalmax
