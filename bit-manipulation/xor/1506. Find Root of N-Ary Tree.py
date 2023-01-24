"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        """
        To reduce the space complexity, we need more insights into the problem setting:
        Actually, we could build upon the insight from the above approach, as follows:
        If we visit all the nodes and all the child nodes, then the root node would be the only node that we visit once and once only. The rest of the nodes would be visited twice.
        Based on the above insight, we could transform the problem into an equivalent problem as follows:
        Given a list of numbers where some of the numbers appear twice, we are asked to find the number that appear only once.
        USES XOR operation on val to find the number that appears twice
        """
        val = 0
        for node in tree:
            val ^= node.val
            for child in node.children:
                val ^= child.val
        
        for node in tree:
            if val == node.val:
                return node
        return None