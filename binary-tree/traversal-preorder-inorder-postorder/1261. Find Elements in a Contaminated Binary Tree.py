# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = set()
        def reconstruct(n, val):
            if not n:
                return
            n.val = val
            self.nodes.add(val)
            if n.left:
                reconstruct(n.left, 2 * val + 1)
            if n.right:
                reconstruct(n.right, 2 * val + 2)
        
        reconstruct(root, 0)


    def find(self, target: int) -> bool:
        return target in self.nodes
