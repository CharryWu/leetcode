# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        def dfs(n, p, isLeft):
            if not n:
                return
            dfs(n.left, n, True)
            dfs(n.right, n, False)
            if n.val in to_delete:
                if isLeft:
                    p.left = None
                else:
                    p.right = None
                if n.left:
                    res.append(n.left)
                if n.right:
                    res.append(n.right)
            
        dummy = TreeNode(left=root)
        dfs(root, dummy, True)
        if dummy.left:
            res.append(dummy.left)
                    
        return res
