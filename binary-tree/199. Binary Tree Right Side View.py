# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while len(q) > 0:
            right = None
            for i in range(len(q)):
                top = q.popleft()
                right = top
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            if right:
                res.append(right.val)
        return res
