# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = None
        
        def dfs(n):
            nonlocal res
            if not n or res:
                return
            if n.val == val:
                res = n
                return
            elif val < n.val:
                dfs(n.left)
            else:
                dfs(n.right)
        dfs(root)
        return res
