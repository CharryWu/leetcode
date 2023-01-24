# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode() # 存小于x的节点
        dummy2 = ListNode() # 存大于x的节点
        p1, p2 = dummy1, dummy2 # p1, p2 指针生成链表
        p = head # 遍历原链表，合并两个有序链表的逻辑
        # 将一个链表分解成两个链表
        while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            # 断开原链表中每个节点的next 指针
            temp = p.next
            p.next = None
            p = temp
            
        # 链接两个链表
        p1.next = dummy2.next
        return dummy1.next
