# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head1, head2):
        dummy = ListNode(0, None)
        cur = dummy
        while head1 or head2:
            if head1 == None:
                cur.next = head2
                break
            elif head2 == None:
                cur.next = head1
                break
            val1, val2 = head1.val, head2.val
            if val1 <= val2:
                n1 = head1.next
                head1.next = None
                cur.next = head1
                cur = head1
                head1 = n1
            else:
                n2 = head2.next
                head2.next = None
                cur.next = head2
                cur = head2
                head2 = n2

        return dummy.next

    def findMid(self, h):
        fast = slow = h
        slowprev = None
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            slowprev = slow
            slow = slow.next

        return slow, slowprev

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        m, mprev = self.findMid(head)
        mprev.next = None
        merged1 = self.sortList(head)
        merged2 = self.sortList(m)

        return self.merge(merged1, merged2)
