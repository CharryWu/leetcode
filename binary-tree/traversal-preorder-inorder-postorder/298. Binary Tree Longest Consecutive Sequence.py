class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 1 # 只有一个节点的 consecutive path 也是 valid 的
        NONE = float('-inf')
        def traverse(n, pval, count):
            nonlocal res
            if not n:
                return
            if n.val == pval+1:
                res = max(res, count+1)
                traverse(n.left, n.val, count+1)
                traverse(n.right, n.val, count+1)
            else:
                traverse(n.left, n.val, 1)
                traverse(n.right, n.val, 1)
        traverse(root, NONE, 1)
        return res
