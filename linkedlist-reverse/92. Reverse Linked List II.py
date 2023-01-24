class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        successor = None
        def reverseFirstN(cur, n):
            nonlocal successor
            if n == 1:
                successor = cur.next
                return cur
            newhead = reverseFirstN(cur.next, n-1)
            cur.next.next = cur # precond: cur.next 节点的 next 指针指向successor。postcond: 将其修正为指向当前cur 节点
            cur.next = successor # 总是将 next 指针指向第 n+1 节点。之后会被改正的。只有旧的链表头部不会被改正，总效果就是旧的链表头部指向n+1
            return newhead
        
        def recur(head, l, r):
            if l == 1:
                return reverseFirstN(head, r) # 如果 l == 1，就相当于反转链表开头的 r 个元素嘛
            # 如果我们把 第一个节点 的索引视为 1，那么我们是想从第 m 个元素开始反转对吧；如果把 第二个节点 的索引视为 1 呢？那么相对于 head.next，反转的区间应该是从第 m - 1 个元素开始的
            next_node = recur(head.next, l-1, r-1)
            head.next = next_node
            return head # 注意这里return 的是 head，因为 recur 不需要改变顺序
        
        return recur(head, left, right)