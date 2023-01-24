# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def traverse(node):
            if not node:
                return None
            
            if node.val < low: # node val too low, go find the node.val >= low in right subtree and traverse on that node
                cur = node.right
                while cur and cur.val < low:
                    cur = cur.right
                if not cur:
                    return None
                return traverse(cur)
            elif node.val > high: # node val too high, go find the node.val <= high in left subtree and traverse on that node
                cur = node.left
                while cur and cur.val > high:
                    cur = cur.left
                if not cur:
                    return None
                return traverse(cur)
            
            node.left = traverse(node.left)
            node.right = traverse(node.right)
            # low <= node val <= high, condition fulfilled, keep node
            return node
        
        return traverse(root)
