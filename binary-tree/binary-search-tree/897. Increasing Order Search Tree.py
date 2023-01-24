# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        leftmost = root
        while leftmost.left:
            leftmost = leftmost.left
        
        def traverse(node):
            if not node:
                return None, None
            if not node.left and not node.right:
                return node, node

            minnode, maxnode = node, node
            if node.left:
                leftmin, leftmax = traverse(node.left)
                minnode = leftmin
                leftmax.right = node
                node.left = None

            if node.right:
                rightmin, rightmax = traverse(node.right)
                maxnode = rightmax
                node.right = rightmin

            return minnode, maxnode
        
        traverse(root)
        return leftmost