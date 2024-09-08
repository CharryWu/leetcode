"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
"""
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        """
        Use reservoir sampling
        # S has items to sample, R will contain the result
        def ReservoirSample(S[1..n], R[1..k])
        # fill the reservoir array
        for i := 1 to k
            R[i] := S[i]

        # replace elements with gradually decreasing probability
        for i := k+1 to n
            # randomInteger(a, b) generates a uniform integer
            #   from the inclusive range {a, ..., b} *)
            j := randomInteger(1, i)
            if j <= k
                R[j] := S[i]
        """
        k = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include element in reservoir
            if random.randint(1, k) == 1:
                chosen_value = curr.val
            curr = curr.next
            k += 1
        return chosen_value
