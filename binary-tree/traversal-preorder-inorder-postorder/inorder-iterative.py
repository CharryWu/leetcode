from collections import deque
 
 
# Data structure to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Iterative function to perform inorder traversal on the tree
def inorderIterative(root):
 
    # create an empty stack
    stack = deque()
 
    # start from the root node (set current node to the root node)
    curr = root
 
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
            print(curr.data, end=' ')
 
            curr = curr.right