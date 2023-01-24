class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        while n > 0:
            p1 = p1.next
            n -= 1
        
        p2 = head
        dummy = ListNode(0, head)
        prev = dummy
        while p1:
            p1 = p1.next
            p2 = p2.next
            prev = prev.next
            
        
        prev.next = p2.next
        
        return dummy.next
