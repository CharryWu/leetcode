# coding=utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
def isPalindrome(self, head: ListNode) -> bool:
    dummy_head = ListNode(0, head)
    fast = slow = dummy_head
    while fast != None:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    print(slow)

    nextnode = slow.next
    slow.next = None # 这里必须置空，否则会出现cycle
    # 若不置空，在第一次循环之后 slow <- -> nextnode
    while nextnode:
        tmp = nextnode
        nextnode = nextnode.next
        tmp.next = slow
        slow = tmp
    print(slow)
    head = dummy_head.next
    while head != slow:
        print(head.val, slow.val)
        if head.val != slow.val:
            return False
        head = head.next
        slow = slow.next
    return True
"""
class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        # 如果有奇数个节点，slow最终停在中间那个。如果偶数个节点，会停在后半部分第一个节点
        while fast and fast.next: # fast and fast.next 检查的是当前区间内的节点
            fast = fast.next.next
            slow = slow.next
        # postcond: 如果链表是 1 2 3 4，则循环结束 fast 指向 None，而 slow 指向 3

        # 链表后半部分反转
        # 一般需要三个指针来实现：一个指向前一个节点prev，一个指向当前节点slow，一个指向下一个节点nxt（可能为空）
        # 每次循环改变当前节点 slow.next 的指向
        prev = None # 之后会被 assigne 给 slow.next
        while slow:
            # 先更新next，再更新 slow.next，再更新prev 和 slow 本身
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # postcond：slow = None，指向原链表末尾的 None，而 prev 指向原链表最后一个元素

        # 从两头向中间检查。这时链表后半部分已被反转，且后半部分原来的第一个节点 next 指向 None
        while prev: # while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(
    Solution().isPalindrome(head)
)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(
    Solution().isPalindrome(head)
)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(
    Solution().isPalindrome(head)
)