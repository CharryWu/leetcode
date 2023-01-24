class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        foundP, foundQ = False, False

        """
        这题只要把 235. 二叉搜索树的最近公共祖先 的解法稍微改一下就行了。

        235. 二叉搜索树的最近公共祖先 说 p 和 q 必然存在二叉树中，而这道题中 p, q 可能不存在，所以需要遍历整棵二叉树才能判断公共祖先是否存在。

        所以可以用变量 foundP 和 foundQ 记录 p 和 q
        """
        def dfs(n):
            if not n:
                return None
        
            # 注意这里的 dfs 顺序，需要在return之前 遍历整棵二叉树才能判断公共祖先是否存在。
            left = dfs(n.left)
            right = dfs(n.right)

            nonlocal p
            nonlocal q
            if n == p:
                nonlocal foundP
                foundP = True
                return n
            if n == q:
                nonlocal foundQ
                foundQ = True
                return n
            
            # 情况 1，如果 p 和 q 都在以 root 为根的树中，那么 left 和 right 一定分别是 p 和 q（从 base case 看出来的）。
            if left and right: # 左右子树存在 p 和 q
                return n
            # 情况 2，左右子树都找不到 p 或 q，直接返回 null 表示当前子树不符合题目条件
            if not left and not right:
                return None
            # 情况 3，如果 p 和 q 只有一个存在于 root 为根的树中，函数返回该节点。
            return left if left else right

        res = dfs(root)
        if foundP and foundQ:
            return res
        else:
            return None