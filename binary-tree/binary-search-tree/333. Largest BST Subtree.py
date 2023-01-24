class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        def dfs(n): # return (min, max, node_count) in tree with n as root, and update res
            """
            定义：输入一棵二叉树，如果这棵二叉树不是 BST，则返回 null，
            如果这棵树是 BST，则返回三个数：
            第一个数是这棵 BST 中的最小值，
            第二个数是这棵 BST 中的最大值，
            第三个数是这棵 BST 的节点总数
            """
            if not n:
                return float('inf'), float('-inf'), 0
            
            left = dfs(n.left)
            right = dfs(n.right)
            
            if (not left) or (not right):
                return None
            leftmin, leftmax, leftcount = left
            rightmin, rightmax, rightcount = right
            
            nonlocal res
            if leftmax < n.val < rightmin:
                # 以 n 为根的二叉树是 BST
                nmin = min(leftmin, n.val) # 左树有可能存在比 n.val 还要小的节点
                nmax = max(rightmax, n.val) # 右树有可能存在比 n.val 还要大的节点
                ncount = leftcount + rightcount + 1
                res = max(res, ncount)
                # 更新全局变量，记录 BST 的最大节点个数
                return nmin, nmax, ncount
            
            return None
        
        dfs(root)
        return res
