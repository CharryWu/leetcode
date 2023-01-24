# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        n = len(arr)
        def traverse(node, i):
            nonlocal n
            if not node or i == n:
                return False
            
            if not node.left and not node.right:
                return i == n-1 and arr[i] == node.val
            if node.val != arr[i]:
                return False
            
            if traverse(node.left, i+1) or traverse(node.right, i+1):
                return True
            
            return False
        
        return traverse(root, 0)
                