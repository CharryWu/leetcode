class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        dummy = ListNode(val=0, next = head)
        slowpre = dummy
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            slowpre = slowpre.next
            slow = slow.next
        
        slowpre.next = slow.next
        return dummy.next
