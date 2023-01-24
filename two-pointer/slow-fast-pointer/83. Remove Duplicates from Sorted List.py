# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow, fast = head, head
        while fast:
            if fast.val != slow.val:
                slow.next = fast # nums[slow] = nums[fast];
                slow = slow.next # slow++;
            fast = fast.next # fast++
        
        slow.next = None # 断开与后面重复元素的连接
        return head