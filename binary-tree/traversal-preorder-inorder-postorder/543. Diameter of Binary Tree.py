# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(n):
            nonlocal res
            if not n:
                return 0
            left_depth = traverse(n.left)
            right_depth = traverse(n.right)
            
            res = max(res, left_depth+right_depth)
            
            return max(left_depth, right_depth)+1
        
        traverse(root)
        return res

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         """
#         解决这题的关键在于，每一条二叉树的「直径」长度，就是一个节点的左右子树的最大深度之和。

#         """
#         def dfs(root):
#             if not root:
#                 return 0

#             hleft, hright = 0, 0
#             diameter_left, diameter_right = 0, 0
#             if root.left:
#                 hleft, diameter_left = dfs(root.left)
#             if root.right:
#                 hright, diameter_right = dfs(root.right)

#             return max(hleft, hright) + 1, max(diameter_left, diameter_right, hleft+hright)
        
#         h, diameter = dfs(root)
        
#         return diameter

