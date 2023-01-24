class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = ListNode(0, head)
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            else:
                return False
            if fast == slow:
                return True
            slow = slow.next
            
        return False

