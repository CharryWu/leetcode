# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    def mergeTwo(self, head1, head2):
        dummy = ListNode(0)
        cur = dummy

        # Iterate through both linked lists
        while head1 and head2:
            # Add the smaller node to the merged list
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        # If any list is left, append it to
        # the merged list
        if head1:
            cur.next = head1
        else:
            cur.next = head2

        # Return the merged list starting
        # from the next of dummy node
        return dummy.next

    """
    Merge linked lists in array[i:j+1]
    Accepts:
        arr - array of linked list
        i - left index in arr, inclusive
        j - right index in arr, inclusive
    Returns - head of merged list
    """
    def mergeListsRecur(self, i, j, arr):
        # If single linked list, return its head since it's sorted already
        if i == j:
            return arr[i]
        # Find the middle list
        mid = i + (j - i) // 2 # [0,1,2] being 1: merge(merge(0+1), 2)
        # [0,1,2,3] being merge(merge(0,1),merge(2,3))
        # Merge lists from i to mid
        head1 = self.mergeListsRecur(i, mid, arr)
        # Merge lists from mid+1 to j
        head2 = self.mergeListsRecur(mid + 1, j, arr)
        # Merge the above 2 lists
        head = self.mergeTwo(head1, head2)
        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Base case for 0 lists to merge
        if len(lists) == 0:
            return None
        return self.mergeListsRecur(0, len(lists) - 1, lists)
