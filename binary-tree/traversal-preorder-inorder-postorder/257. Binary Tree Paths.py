class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        res = []
        
        def traverse(n):
            if not n:
                return
            path.append(str(n.val))
            if not n.left and not n.right:
                res.append('->'.join(path))
            traverse(n.left)
            traverse(n.right)
            path.pop()
        
        traverse(root)
        return res