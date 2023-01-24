# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        这道题需要用到「遍历」的思维。
        维护一个外部累加变量 sum，在遍历 BST 的过程中增加 sum，同时把 sum 赋值给 BST 中的每一个节点，就将 BST 转化成累加树了。
        但是注意顺序，正常的中序遍历顺序是先左子树后右子树，这里需要反过来，先右子树后左子树。
        """
        s = 0
        def traverse(n):
            nonlocal s
            if not n:
                return
            rsum = traverse(n.right)
            s += n.val
            n.val = s
            lsum = traverse(n.left)

        
        traverse(root)
        return root