"""
Pair up \text{k}k lists and merge each pair.

After the first pairing, \text{k}k lists are merged into k/2k/2 lists with average 2N/k2N/k length, then k/4k/4, k/8k/8 and so on.

Repeat this procedure until we get the final sorted linked list.

Thus, we'll traverse almost NN nodes per pairing and merging, and repeat this procedure about \log_{2}{k}log 
2
​
 k times.
"""
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not n:
            return None
    
        
        def merge2Lists(l1, l2):
            head = point = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    point.next = l1
                    l1 = l1.next
                else:
                    point.next = l2
                    l2 = l1
                    l1 = point.next.next
                point = point.next
            if not l1:
                point.next=l2
            else:
                point.next=l1
            return head.next
        
        interval = 1
        while interval < n:
            for i in range(0, n-interval, interval*2):
                lists[i] = merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        
        return lists[0]
