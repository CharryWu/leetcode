# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = deque()
        self.curr = root

    def next(self) -> int:
        retval = None
        # if the current node exists, push it into the stack (defer it)
        # and move to its left child
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        else:
            # otherwise, if the current node is None, pop an element from the stack,
            # print it, and finally set the current node to its right child
            self.curr = self.stack.pop()
            retval = self.curr.val
            self.curr = self.curr.right
        return retval

    def hasNext(self) -> bool:
        if not self.stack and not self.curr:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()