# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def swap(n1, n2, n1prev, n2prev):
    if n1 == n2:
        return
    if n1prev:
        n1prev.next = n2
    if n2prev:
        n2prev.next = n1
    
    # swap remaining pointers    
    temp = n1.next
    n1.next = n2.next
    n2.next = temp

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        dummy = ListNode(next=head)
        prev = dummy
        cur = head

        while cur:
            smallest = cur
            smallest_prev = prev
            temp = cur.next
            temp_prev = cur
            while temp:
                if temp.val < smallest.val:
                    smallest = temp
                    smallest_prev = temp_prev
                temp_prev = temp
                temp = temp.next
            swap(cur, smallest, prev, smallest_prev)

            prev = smallest
            cur = smallest.next

        return dummy.next