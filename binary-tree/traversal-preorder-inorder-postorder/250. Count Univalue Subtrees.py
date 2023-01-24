# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        NON_EQUAL = float('-inf')
        res = 0
        def traverse(n):
            """
            定义：输入一棵二叉树，如果这棵二叉树的所有节点值都相同，则返回它们的值
            如果这棵二叉树的所有节点的值不是相同的，则返回 NON_EQUAL。
            如果有任何一棵子树的值不相同，那么以 n 为根的这棵树的值肯定不可能全部相同
            （因为题目说节点的正常取值为 [-1000, 1000]，所以 -1001 是个特殊值）
            """
            nonlocal res
            # 先算出左右子树的值是否全部相同
            left, right = n.val, n.val # 初始值设置成当前节点n的值，如果子节点不存在则不用比较
            if n.left:
                left = traverse(n.left)
            if n.right:
                right = traverse(n.right)
            # 如果有任何一棵子树的值不相同，那么以 n 为根的这棵树的值肯定不可能全部相同
            if left == NON_EQUAL or right == NON_EQUAL:
                return NON_EQUAL
            # 如果左右子树的值都相同，且等于 n.val，则说明以 n 为根的二叉树是一棵所有节点都相同的二叉树
            if left == right == n.val:
                res += 1
                return n.val
            # 否则，以 n 为根的二叉树不是一棵所有节点都相同的二叉树
            return NON_EQUAL
        
        traverse(root)
        return res