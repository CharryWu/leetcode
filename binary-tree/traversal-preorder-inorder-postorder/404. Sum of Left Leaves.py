class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def traverse(n, p):
            nonlocal res
            if not n:
                return
            if not n.left and not n.right:
                if n == p.left:
                    res += n.val
            
            traverse(n.left, n)
            traverse(n.right, n)
        traverse(root, TreeNode(right=root))
        return res