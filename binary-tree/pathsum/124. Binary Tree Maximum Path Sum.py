# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf') # 可能整棵树都是负数
        def dfs(n):
            nonlocal res
            if not n:
                return 0
            left_path = dfs(n.left)
            right_path = dfs(n.right)
            # path必须不为空，所以至少包含一个节点
            # 将left_path和right_path设置为空，可以将其排除在取res 最值 res=max(...) 的计算之外
            if not n.right:
                right_path = float('-inf')
            if not n.left:
                left_path = float('-inf')
            res = max(
                res,
                n.val, # 若左右子树 path_sum 都是负数，不如从当前节点开始path，而不是从左右子树开始
                left_path, right_path,
                n.val+left_path, n.val+right_path,
                n.val+left_path+right_path
            )
            
            return max(left_path, right_path, 0) + n.val # 注意这里需要将0 也包含进去。若n为叶子节点，避免返回数值为float('-inf')

        dfs(root) # The number of nodes in the tree is in the range [1, 3 * 104]
        
        return res
