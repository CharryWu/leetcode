# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        In-order traversal of bst gives a sorted array
        We use iterative solution (using external stack)
        """
        n = 0 # num of elements we visited
        stack = []
        cur = root

        #### check if cur OR stack is null
        while cur or stack: # traversing until visited every node in bst
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
