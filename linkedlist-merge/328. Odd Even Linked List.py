# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy1, dummy2 = ListNode(0), ListNode(0)
        l1, l2 = dummy1, dummy2
        first_cur, second_cur = head, head.next
        while first_cur or second_cur:
            if first_cur:
                l1.next = first_cur
                l1 = l1.next
                l1.next = None
                if second_cur:
                    first_cur = second_cur.next
                else:
                    break

            if second_cur:
                l2.next = second_cur
                l2 = l2.next
                l2.next = None
                if first_cur:
                    second_cur = first_cur.next
                else:
                    break

        l1.next = dummy2.next
        return dummy1.next