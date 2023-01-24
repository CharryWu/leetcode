class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        curval = root.val
        # 一直向下递归，直到p 和 q 不在root的同一颗子树为止（或 p q 中一个就是root 为止）
        if p.val < curval and q.val < curval:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > curval and q.val > curval:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root