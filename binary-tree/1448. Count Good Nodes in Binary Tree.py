class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # pre-order traversal
        def dfs(node, maxVal):
            # `maxVal` is the maximum value
            # we've seen so far from root on current path
            # returns the count of good nodes at current subtree
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)
