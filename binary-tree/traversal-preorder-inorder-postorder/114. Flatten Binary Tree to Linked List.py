# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        ##### postcondition: root 的左右子树已经被拉平成一条链表
        left, right = root.left, root.right # 保存原先左右子树节点
        root.left, root.right = None, left # 将左子树作为右子树
        p = root
        while p.right:
            p = p.right
        p.right = right # 将原先右子树接到当前右子树的末端
