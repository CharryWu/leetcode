# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = float('-inf')
        def traverse(node):
            """
            返回 (子树总和, 子树节点数量)
            """
            nonlocal res
            if not node:
                return 0, 0
            
            leftsum, leftcount = traverse(node.left)
            rightsum, rightcount = traverse(node.right)

            if leftcount > 0:
                res = max(res, leftsum / leftcount)

            if rightcount > 0:
                res = max(res, rightsum / rightcount)

            cursum = leftsum + rightsum + node.val
            curcount = leftcount + rightcount + 1
            res = max(res, cursum / curcount)
            return cursum, curcount

        traverse(root)
        return res

