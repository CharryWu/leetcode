class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        O(n) memory solution is trivial, so no fun in that.

        We could use slow and fast pointers to determine the middle of the list. We then reverse the list starting from the middle, so we can easily iterate through twins.

        Note that we can do the reversal again to restore the original list (omitted for simplicity).
        """
        slow, fast = head, head
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            slow = slow.next
        
        pre = None
        n = slow.next
        while slow:
            slow.next = pre
            pre, slow = slow, n
            if n: # 注意这里n可能为空，即循环结束条件
                n = n.next
        
        res = 0
        head2 = pre
        while head.next:
            res = max(res, head.val + head2.val)
            head, head2 = head.next, head2.next
        return res
        
