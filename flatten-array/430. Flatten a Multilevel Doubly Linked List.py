"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def traverse(head):
            if not head:
                return None, None
            
            cur = head
            prev = None
            while cur:
                if cur.child:
                    child, childend = traverse(cur.child)
                    cur.child = None
                    nxt = cur.next
                    if nxt:
                        nxt.prev = childend
                        childend.next = nxt
                    cur.next = child
                    child.prev = cur
                if cur:
                    prev = cur
                cur = cur.next
            return head, prev
        
        newhead, newend = traverse(head)
        return newhead