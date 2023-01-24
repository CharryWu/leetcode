from collections import defaultdict
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        seen = defaultdict(int)
        dummy = ListNode(next=head)
        cur, prev = head, dummy
        while cur:
            seen[cur.val] += 1
            cur, prev = cur.next, prev.next

        cur, prev = head, dummy
        while cur:
            if seen[cur.val] > 1:
                tmp = cur.next
                prev.next = tmp
                cur.next = None
                cur = tmp
            else:
                cur, prev = cur.next, prev.next

        return dummy.next