# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not n1 and not n2:
            return None
        elif n1 and not n2:
            return n1
        elif n2 and not n1:
            return n2
        elif n1 and n2:
            cur = TreeNode(val=n1.val+n2.val)
            cur.left = self.mergeTrees(n1.left, n2.left)
            cur.right = self.mergeTrees(n1.right, n2.right)
            return cur

        return None