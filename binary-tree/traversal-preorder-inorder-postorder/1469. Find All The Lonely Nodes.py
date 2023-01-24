# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def traverse(n, isLonely):
            if not n:
                return
            
            if isLonely:
                res.append(n.val)

            if n.left and not n.right:
                traverse(n.left, True)
            elif n.right and not n.left:
                traverse(n.right, True)
            elif n.left and n.right:
                traverse(n.left, False)
                traverse(n.right, False)
            return
        
        traverse(root, False)
        return res