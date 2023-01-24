# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        """
        定义：输入一棵 BST 和一个 target，返回两棵 BST 的根节点，
        第一棵所有节点都小于等于 target，第二棵所有节点都大于 target
        """
        if not root:
            return [None, None]
        res = [None, None]
        if root.val <= target: # root 必然是第一棵 BST 的根节点
            res[0] = root
            right = self.splitBST(root.right, target) # 第二棵 BST 的根节点需要去右子树算
            res[1] = right[1]
            root.right = right[0] # 保证 root 的右子树都是小于 target 的
        else: # root 必然是第二棵 BST 的根节点
            res[1] = root
            left = self.splitBST(root.left, target) # root 必然是第二棵 BST 的根节点
            res[0] = left[0]
            root.left = left[1] # 保证 root 的左子树都是大于 target 的
        return res