# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        sorthead = dummy

        while head:
            n = head
            head = head.next
            n.next = None
            # find the pos to insert
            while sorthead.next and sorthead.next.val < n.val:
                sorthead = sorthead.next
            # postcond: sorthead.val < n.val
            # add node n to the linked list beginning by sorthead
            prevn = sorthead.next
            sorthead.next = n
            n.next = prevn
            sorthead = dummy

        return dummy.next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # cut the list into two halves
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)

        return self.merge(l, r)
    
    def merge(self, l, r):
        if l is None:
            return r
        elif r is None:
            return l
        
        dummy = ListNode(0)
        head = dummy
        
        while l and r:
            if l.val <= r.val:
                head.next = l
                l = l.next
            else:
                head.next = r
                r = r.next
            head = head.next
            
        head.next = l if r is None else r
        return dummy.next