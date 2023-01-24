# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def traverse(n):
            nonlocal res
            if not n:
                return 0
            lsum = traverse(n.left)
            rsum = traverse(n.right)
            res += abs(lsum-rsum)
            return lsum + rsum + n.val
        traverse(root)
        return res