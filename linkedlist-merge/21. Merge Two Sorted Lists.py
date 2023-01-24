# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        l1, l2 = list1, list2
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                cur, l1 = l1, l1.next
            else:
                cur.next = l2
                cur, l2 = l2, l2.next
            
        
        if not l1:
            cur.next = l2
        else:
            cur.next = l1
        
        return dummy.next
