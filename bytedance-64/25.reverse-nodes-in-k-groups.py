# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, start, end):
        """
        n1 <- n2    n3    n4 -> n5
        s     prev  tmp    n     e

        Use tmp, prev, n pointers
        init value: prev, tmp, n = None, start, start.next

        Update while there's more n node to be assigned:
            tmp.next = prev # the line that does the job
            # reassign prev, tmp, n from left to right
            prev = tmp
            tmp = n
            n = n.next

        """
        s, e = start, end
        prev = None
        cur = s

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return (e, s)

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy
        cnt = 0
        # fast slow 指向 当前 k group 末尾，上个 kgroup 末尾
        while fast.next:
            fast = fast.next
            cnt += 1
            if cnt % k == 0:
                nextkgrouphead = fast.next
                curkgrouphead = slow.next
                # 断开 fast, slow 和 下个 kgroup, 当前 kgroup 链接
                slow.next, fast.next = None, None
                # fast points to cur kgroup tail
                newstart, newtail = self.reverse(curkgrouphead, fast)
                # 断开
                slow.next = newstart
                newtail.next = nextkgrouphead
                fast = slow = newtail

        return dummy.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

Solution().reverseKGroup(l1, 2)
