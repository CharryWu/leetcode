# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        ll = []
        def dfs(n):
            if not n:
                return
            dfs(n.left)
            ll.append(n.val)
            dfs(n.right)
        
        dfs(root)
        
        if len(ll) < 2:
            return False
        
        seen = {}
        for i, num in enumerate(ll):
            # 注意这里 k-num in seen 要先被判断
            if k - num in seen:
                return True
            if num not in seen:
                seen[num] = i
            
        return False
