# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        
        def traverse(n):
            if not n:
                return
            res.append('(')
            res.append(str(n.val))

            # we cannot omit the first parenthesis pair
            # to break the one-to-one mapping relationship
            # between the input and the output.
            if not n.left and n.right:
                res.append('(')
                res.append(')')
            traverse(n.left)
            traverse(n.right)
            
            res.append(')')
        
        traverse(root)
        
        return ''.join(res[1:-1])
