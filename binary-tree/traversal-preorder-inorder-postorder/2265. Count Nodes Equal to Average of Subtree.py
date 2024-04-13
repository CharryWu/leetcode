# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recur(node):
            nonlocal res
            if not node:
                return 0, 0
            lefts, leftcount = recur(node.left)
            rights, rightcount = recur(node.right)
            thissum = lefts + rights + node.val
            thiscount = leftcount + rightcount + 1
            # print(node.val, thissum, thiscount)
            if node.val == int(thissum / thiscount):
                res += 1
            return thissum, thiscount
        recur(root)
        return res
