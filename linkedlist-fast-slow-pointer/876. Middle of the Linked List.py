class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            slow = slow.next
        
        return slow
