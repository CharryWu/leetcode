# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        def traverse(node, pval):
            """
            定义：计算以 root 为根的这棵二叉树中，从 root 开始值为 parentVal 的最长树枝长度
            """
            nonlocal res
            if not node:
                return 0
            
            # 利用函数定义，计算左右子树值为 root.val 的最长树枝长度
            leftlen = traverse(node.left, node.val)
            rightlen = traverse(node.right, node.val)

            # 在后序遍历的位置更新 res
            # 利用函数定义，计算左右子树值为 root.val 的最长树枝长度
            # 同值路径就是左右同值树枝长度之和
            res = max(res, leftlen + rightlen)
            if node.val != pval: # 如果 root 本身和上级值不同，那么整棵子树都不可能有同值树枝
                return 0
            # 如果 root 本身和上级值不同，那么整棵子树都不可能有同值树枝
            # 以 root 为根的二叉树从 root 开始值为 parentVal 的最长树枝长度
            # 等于左右子树的最长树枝长度的最大值加上 root 节点本身
            return 1 + max(leftlen, rightlen)

        traverse(root, root.val)
        return res