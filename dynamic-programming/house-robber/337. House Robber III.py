class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def traverse(node):
            if not node:
                return 0
            # 利用备忘录消除重叠子问题
            if node in memo:
                return memo[node]
            # 抢，然后去下下家
            do_it = node.val \
                + ((traverse(node.left.left) + traverse(node.left.right)) if node.left else 0) \
                + ((traverse(node.right.left) + traverse(node.right.right)) if node.right else 0)
            # 不抢，然后去下家
            not_do = traverse(node.left) + traverse(node.right)

            res = max(do_it, not_do)
            memo[node] = res
            return res

        return traverse(root)