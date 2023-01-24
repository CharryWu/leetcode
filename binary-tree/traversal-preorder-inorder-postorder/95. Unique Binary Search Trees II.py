# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        类似 96. 不同的二叉搜索树，这题的思路也是类似的，想要构造出所有合法 BST，分以下三步：

        1、穷举 root 节点的所有可能。
        2、递归构造出左右子树的所有合法 BST。
        3、给 root 节点穷举所有左右子树的组合。
        """
        if n == 0:
            return []

        def build(lo, hi):
            """
            构造闭区间 [lo, hi] 组成的 BST
            """
            cur_res = []
            if lo > hi: # base case
                cur_res.append(None)
                return cur_res
            # 1、穷举 root 节点的所有可能。
            for mid in range(lo, hi+1):
                # 2、递归构造出左右子树的所有合法 BST。
                left_trees = build(lo, mid-1)
                right_trees = build(mid+1, hi)
                for lroot in left_trees:
                    for rroot in right_trees:
                        mid_root = TreeNode(mid)
                        mid_root.left = lroot
                        mid_root.right = rroot
                        cur_res.append(mid_root)
            return cur_res
        # 构造闭区间 [1, n] 组成的 BST
        return build(1, n)
