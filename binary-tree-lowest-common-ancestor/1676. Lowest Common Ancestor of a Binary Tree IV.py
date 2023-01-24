class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        def dfs(n):
            if not n:
                return None
            if n in nodes:
                return n
            
            left = dfs(n.left)
            right = dfs(n.right)
        
            if not left and not right:
                return None
            elif left and right:
                return n
            else:
                return left if left else right
        
        res = dfs(root)
        return res
            