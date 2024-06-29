class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            # left and right are boundaries
            # returns True if subtree at `node` is bst, false otherwise
            if not node:
                return True
            if node.val >= right or node.val <= left:
                return False

            # all values in left subtree has to be less than current node
            # all values in right subtree has to be greater than current node
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        return dfs(root, float('-inf'), float('inf'))
