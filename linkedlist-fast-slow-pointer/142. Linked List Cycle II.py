class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        
        if not fast or not fast.next: # 这里也需要检测 fast.next
            return None
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
            
        return slow

