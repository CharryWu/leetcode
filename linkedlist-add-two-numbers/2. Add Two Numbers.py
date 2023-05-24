# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 获取两个链表代表的数
        num1, num2 = 0, 0
        e1, e2 = 0, 0
        while l1:
            num1 += l1.val * (10**(e1))
            e1 += 1
            l1 = l1.next
        while l2:
            num2 += l2.val * (10**(e2))
            e2 += 1
            l2 = l2.next
        
        # 构建相加结果链表
        dummy = ListNode(0)
        cur = dummy
        s = num1+num2
        # 特殊case：计算结果为0时返回0
        if s == 0:
            return ListNode(0)
        while s > 0:
            s, digit = divmod(s, 10)
            cur.next = ListNode(digit)
            cur = cur.next
        return dummy.next
