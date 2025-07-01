# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Reverse using Iteration
    # This solution iterates through the linked list in groups of k nodes,
    # reversing the links within each group.
    # It maintains a pointer to the new head of the reversed list and a tail pointer
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        curr = head
        newHead = None
        tail = None

        while curr:
            oldGroupHead = curr
            prev = None
            nextNode = None
            count = 0

            # Reverse the nodes in the current group
            while curr and count < k:
                nextNode = curr.next # store ptr to next node temporarily
                curr.next = prev # reverse the link
                prev = curr # forward prev ptr to cur node
                curr = nextNode # forward cur ptr to next node
                count += 1

            # If newHead is null, set it to the
            # last node of the first group
            if not newHead:
                newHead = prev # will only assigned once per program

            # Connect last group tail (1 and 3 in below example) to the
            # current reversed group head
            if tail:
                # precondition: prev points to the first node of current group we just reversed (4 or 5 in below example)
                # precondition: tail points to the last node of the reversed previous group (1 or 3 in below example)
                # precondition: curr points to the first node of the next group (5)
                # precondition: oldGroupHead points to the first node of current group pre-reversal (1 or 3 in below example)
                tail.next = prev # 2->1 => 4->3 => 5

            # Move tail to the end   of
            # the reversed group
            tail = oldGroupHead

        return newHead


    # Reverse using Stack
    # This is an alternative solution using a stack to reverse the nodes in k-groups.
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        stack = []
        curr = head
        prev = None

        while curr:

            # Terminate the loop when either
            # current == None or count >= k
            count = 0
            # add current group nodes to the stack
            while curr and count < k:
                stack.append(curr)
                curr = curr.next
                count += 1

            if len(stack) < k:
                if prev:
                    prev.next = stack[0]
                else:
                    head = stack[0]
                prev = stack[-1] if stack else None  # Update prev to the last node
                stack.clear()  # Clear the stack for the next group
                continue # If less than k nodes, do not reverse (last group)

            # Now pop the elements from the stack one by one
            while stack:


                if not prev:
                    prev = stack.pop() # assign last node of current group to prev
                    head = prev # last node of current group becomes the new head
                else:
                    # e.g. input is 1->..->10
                    # 1->2->3->4->5 becomes 1<-2<-3<-4<-5
                    # Then 5->4->3->2->1(prev) -> [10 <- 9 <- 8 <- 7 <- 6] ([] denotes stack)
                    prev.next = stack.pop()      # |
                    prev = prev.next             # v
                    #                             None

        # Set the next pointer of the last node to None
        prev.next = None

        return head
