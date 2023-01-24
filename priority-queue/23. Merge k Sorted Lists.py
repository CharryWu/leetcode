import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not n:
            return None
        h = []
        for i, n in enumerate(lists):
            if n:
                heapq.heappush(h, (n.val, i))

        dummy = ListNode()
        res = dummy
        while len(h) > 0:
            topVal, i = heapq.heappop(h)
            res.next = ListNode(topVal)
            res = res.next

            nextNode = lists[i].next            
            if nextNode:
                heapq.heappush(h, (nextNode.val, i))
                lists[i] = nextNode
        return dummy.next
