# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def traverse(n):
            if not n:
                return None
            if n.val == target.val:
                return n
            
            left = traverse(n.left)
            if left:
                return left
            right = traverse(n.right)
            if right:
                return right
            return None
        
        return traverse(cloned)