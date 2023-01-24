"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""
from collections import deque
MARKER = ')'
SPLITTER = ','
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        items = []

        def preorder(node):
            nonlocal items
            if not node:
                return
            items.append(str(node.val))
            for child in node.children:
                preorder(child)
            items.append(MARKER)

        preorder(root)
        return SPLITTER.join(items)

	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        tokens = deque(data.split(SPLITTER))
        root = Node(int(tokens.popleft()), [])

        def helper(node):

            if not tokens:
                return

            # 只要tokens 里面还有节点没被pop，那么其之后一定包含至少一个 SPLITTER 子元素终结符
            while tokens[0] != MARKER: # add child nodes with subtrees
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)

            tokens.popleft()        # discard the "#"

        helper(root)
        return root