# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        定义：删除 BST 中小于 low 和大于 high 的所有节点，返回结果 BST
        """
        if not root:
            return None

        if root.val < low:
            # 直接返回 root.right
            # 等于删除 root 以及 root 的左子树
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            # 直接返回 root.left
            # 等于删除 root 以及 root 的右子树
            return self.trimBST(root.left, low, high)
        else: # low <= root.val <= high
            # 闭区间 [lo, hi] 内的节点什么都不做
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)

            return root
