# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def traverse(n):
            if not n:
                return ['#']
            left = traverse(n.left)
            right = traverse(n.right)
            return [str(n.val)] + left + right

        return ','.join(traverse(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = deque(data.split(','))

        def traverse(str_list):
            if not str_list:
                return None
            
            first = str_list.popleft()
            if first == '#':
                return None
            root = TreeNode(int(first))
            root.left = traverse(str_list)
            root.right = traverse(str_list)

            return root
        
        return traverse(data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))