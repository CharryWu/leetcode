class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        # backtracking 用回溯算法
        def dfs(n, remain):
            if not n:
                return

            nonlocal path
            path.append(n.val) # 注意，这里需要先将 val 放进path 里面，不然添加到 result 的时候会少放最后的叶子节点
            if not n.left and not n.right and remain == n.val: # 这里需要检查是否为叶子节点。若 remain == n.val 但n不是叶子节点，也不能算作valid path
                nonlocal res
                res.append(list(path))

            
            dfs(n.left, remain - n.val)
            dfs(n.right, remain - n.val)
            path.pop()
            return

        dfs(root, targetSum)
        return res
            
