# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        """
        This question equates to finding if there's any value that's diff from root.val, and closest to root
        If there is such value, return it 
        """
        def traverse(node, val):
            if not node:
                return float('inf')
            
            left = traverse(node.left, val)
            right = traverse(node.right, val)

            candidate = float('inf')
            for num in [node.val, left, right]:
                if num != val and num < candidate:
                    candidate = num
            return candidate

        res = traverse(root, root.val)
        return res if res != float('inf') and res != root.val else -1