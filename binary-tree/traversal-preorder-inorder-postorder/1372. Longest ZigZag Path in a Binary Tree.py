# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        二叉树的递归分为「遍历」和「分解问题」两种思维模式，这道题需要用到「分解问题」的思维，而且要用到后序位置的妙用
        首先，我们先明确一下名词的含义，便于讲解：

        如果一个从上到下的交错路径的开头是从右到左的，称之为「左交错路径」，反之成为「右交错路径」。
        这样的话，一个节点 x 能够产生的交错路径就能分解到左右子树：
        1、x 的左子树的「右交错路径」+ 节点 x = x 的「左交错路径」
        2、x 的右子树的「左交错路径」+ 节点 x = x 的「右交错路径」
        比较 x 的左右交错路径，即可算出以 x 开头的最长交错路径。
        对二叉树上的所有节点计算交错路径长度，即可得到最长的交错路径长度。
        所以我们定义一个 getPathLen 函数计算并返回一个节点的左右交错路径长度，然后在后序位置上更新全局最大值。
        """
        res = 0
        def traverse(node):
            """
            输入二叉树的根节点 root，返回两个值
            第一个是从 root 开始向左走的最长交错路径长度，
            第一个是从 root 开始向右走的最长交错路径长度
            """
            nonlocal res
            if not node:
                return -1, -1 # 注意这里返回的是 -1，因为叶子节点的path长度为0
            left = traverse(node.left)
            right = traverse(node.right)
            # 后序位置，根据左右子树的交错路径长度推算根节点的交错路径长度
            node_leftpath_len = left[1] + 1
            node_rightpath_len = right[0] + 1
            # 更新全局最大值
            res = max(res, node_leftpath_len, node_rightpath_len)
            return node_leftpath_len, node_rightpath_len

        traverse(root)
        return res
            