# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, start, end):
        s, e = start, end
        prev, cur = None, s
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        
        return (e, s)

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right, cnt, k = dummy, dummy, 1, 1

        while right.next:
            cnt -= 1
            right = right.next

            if cnt == 0 or right.next == None:
                ss, ee = left.next, right.next

                ne = right # 只有在偶数组或者最后一组为偶数才反转
                if (k - cnt) % 2 == 0: # 只有
                    left.next, right.next = None, None
                    ns, ne = self.reverse(ss, right)
                    left.next, ne.next = ns, ee

                left = right = ne
                k += 1
                cnt = k

        return dummy.next