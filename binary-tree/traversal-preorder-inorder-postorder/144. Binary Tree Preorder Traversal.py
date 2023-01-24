class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        动态规划思路
        """
        if not root:
            return []
        res = [root.val]
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res