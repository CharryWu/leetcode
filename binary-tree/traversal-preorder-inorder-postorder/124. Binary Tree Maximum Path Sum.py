# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def traverse(n):
            """
            定义：计算从根节点 root 为起点的最大单边路径和
            """
            nonlocal res
            if not n:
                return 0
            # 倘若当前节点有一颗子树pathsum 为负数，则计算结果不用包含该子树
            left_sum = max(0, traverse(n.left)) # 当 max(0, ...) == 0，该子树的sum不被算入pathsum 里面
            right_sum = max(0, traverse(n.right))
            # 后序遍历位置，顺便更新最大路径和
            path_sum = n.val + left_sum + right_sum
            res = max(res, path_sum)
            
            # 实现函数定义，左右子树的最大单边路径和加上根节点的值
            # 就是从根节点 root 为起点的最大单边路径和
            return max(left_sum, right_sum) + n.val # 注意这里不包含path_sum，我们只要单边路径的最大值，双边路径最大值不符合定义
        # 计算单边路径和时顺便计算最大路径和
        traverse(root)
        return res

# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         res = float('-inf') # 可能整棵树都是负数
#         def dfs(n):
#             nonlocal res
#             if not n:
#                 return 0
#             left_path = dfs(n.left)
#             right_path = dfs(n.right)
#             # path必须不为空，所以至少包含一个节点
#             # 将left_path和right_path设置为空，可以将其排除在取res 最值 res=max(...) 的计算之外
#             if not n.right:
#                 right_path = float('-inf')
#             if not n.left:
#                 left_path = float('-inf')
#             res = max(
#                 res,
#                 n.val, # 若左右子树 path_sum 都是负数，不如从当前节点开始path，而不是从左右子树开始
#                 left_path, right_path,
#                 n.val+left_path, n.val+right_path,
#                 n.val+left_path+right_path
#             )
            
#             return max(left_path, right_path, 0) + n.val # 注意这里需要将0 也包含进去。若n为叶子节点，避免返回数值为float('-inf')

#         dfs(root) # The number of nodes in the tree is in the range [1, 3 * 104]
        
#         return res
