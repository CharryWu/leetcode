# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, head1, head2):
        dummy = ListNode(0, None)
        cur = dummy
        if not head1 or not head2:
            return head1 or head2
        while head1 and head2:
            if head1.val > head2.val:
                cur.next = head2
                head2 = head2.next
            else:
                cur.next = head1
                head1 = head1.next
            cur = cur.next

        cur.next = head1 or head2
        return dummy.next

    def findMid(self, h):
        dummy = ListNode(0, h)
        fast, slow = dummy.next, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow, slow.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mprev, m = self.findMid(head)
        mprev.next = None
        merged1 = self.sortList(head)
        merged2 = self.sortList(m)

        return self.merge(merged1, merged2)
