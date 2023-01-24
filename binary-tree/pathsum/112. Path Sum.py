class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(n, remain): # 返回当前是否存在，以及当前的剩余所需的
            if not n:
                return False
            if not n.left and not n.right:
                return remain == n.val

            
            if dfs(n.left, remain - n.val):
                return True
            if dfs(n.right, remain - n.val):
                return True
            
            return False

        return dfs(root, targetSum)
            
