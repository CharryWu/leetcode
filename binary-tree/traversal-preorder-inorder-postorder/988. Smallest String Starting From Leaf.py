# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = ''
        
        def traverse(n, path):
            nonlocal res
            if not n:
                return
            newstr = chr(n.val + ord('a')) + path
            if not n.left and not n.right:
                if not res or newstr < res:
                    res = newstr
            
            traverse(n.left, newstr)
            traverse(n.right, newstr)
        
        
        traverse(root, '')
        return res