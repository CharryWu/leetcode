"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
from collections import deque
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        dummy = Node(0)
        prev = dummy

        # create an empty stack
        stack = deque()
        # start from the root node (set current node to the root node)
        curr = root
        last = None

        # if the current node is None and the stack is also empty, we are done
        while stack or curr:
            # if the current node exists, push it into the stack (defer it)
            # and move to its left child
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                # otherwise, if the current node is None, pop an element from the stack,
                # print it, and finally set the current node to its right child
                curr = stack.pop()
                prev.right = curr
                curr.left = prev
                prev = curr
                
                # 最后一个节点：curr 和 stack 都没元素了
                if not stack and not curr.right:
                    last = curr

                curr = curr.right

        last.right = dummy.right
        dummy.right.left = last
        return dummy.right
