# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
MOD = 10**9+7
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def get_sum(n):
            if not n:
                return 0
            return n.val + get_sum(n.left) + get_sum(n.right)
        tree_sum = get_sum(root)

        res = float('-inf')
        def traverse(n):
            nonlocal res
            nonlocal tree_sum
            if not n:
                return 0
            
            left = traverse(n.left)
            right = traverse(n.right)

            res = max(res, left * (tree_sum-left), right * (tree_sum-right))
            return left + right + n.val
        
        traverse(root)
        return res % MOD