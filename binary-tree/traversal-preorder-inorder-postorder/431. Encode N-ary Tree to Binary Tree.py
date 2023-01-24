"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        
        newRoot = TreeNode(root.val)
        children = root.children
        if not children:
            return newRoot
        nchild = len(children)
        newRoot.left = self.encode(children[0])
        curChild = newRoot.left
        for i in range(1, nchild):
            curChild.right = self.encode(children[i])
            curChild = curChild.right
        return newRoot
        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None
        
        root = Node(data.val, [])
        childptr = data.left
        while childptr:
            root.children.append(self.decode(childptr))
            childptr = childptr.right
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))