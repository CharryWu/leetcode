# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy = TreeNode(val=0, left=root)

        def traverse(n, cur_depth):
            if not n:
                return
            if cur_depth == depth-1:
                old_left, old_right = n.left, n.right
                n.left = TreeNode(val=val, left=old_left)
                n.right = TreeNode(val=val, right=old_right)
            elif cur_depth < depth-1:
                traverse(n.left, cur_depth+1)
                traverse(n.right, cur_depth+1)
        traverse(dummy, 0)
        return dummy.left