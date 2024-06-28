"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = { None: None } # old node to new node, edge case, end of list is none
        cur = head
        while cur:
            copy = Node(cur.val) # make copy of node
            mapping[cur] = copy
            cur = cur.next

        # connect nodes with pointers
        cur = head
        while cur:
            # set both `next` and `random` pointers
            copy = mapping[cur]
            copy.next = mapping[cur.next]
            copy.random = mapping[cur.random]
            cur = cur.next
        return mapping[head]
