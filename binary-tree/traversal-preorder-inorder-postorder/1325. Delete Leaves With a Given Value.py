# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def traverse(node, p):
            if not node:
                return
            
            traverse(node.left, node)
            traverse(node.right, node)

            if not node.left and not node.right and node.val == target:
                if p.left == node:
                    p.left = None
                elif p.right == node:
                    p.right = None
        
        dummy = TreeNode(val=target+1, left=root)
        traverse(root, dummy)
        return dummy.left