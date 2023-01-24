# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque([(root, 1)])
        
        while len(queue) > 0:
            top_node, top_level = queue.popleft()
            if len(res) < top_level:
                res.append(top_node.val)
            elif res[top_level-1] < top_node.val:
                res[top_level-1] = top_node.val
            
            if top_node.left:
                queue.append((top_node.left, top_level+1))
            if top_node.right:
                queue.append((top_node.right, top_level+1))
            
        return res