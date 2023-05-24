class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        # 代码结构和addtwonum i 大致相同。不一样的地方在于获取 num1 num2 和 构建linkedlist顺序
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        
        s = num1 + num2
        if s == 0:
            return ListNode(0)
        dummy = ListNode(0)

        while s > 0:
            s, digit = divmod(s, 10)
            oldHead = dummy.next
            dummy.next = ListNode(digit, oldHead)
        return dummy.next
