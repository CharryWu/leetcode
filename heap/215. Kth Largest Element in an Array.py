import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [] # maintain a min heap of k elements, push to heap when see larger one
        n = len(nums)
        for num in nums:
            if len(minheap) < k or num > minheap[0]:
                heapq.heappush(minheap, num)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]

import random
class Solution:
    def findKthLargest(self, nums, k):
        """
        First, we need to choose so-called pivot and partition element of nums into 3 parts:
            elements, smaller than pivot, equal to pivot and bigger than pivot. (sometimes two groups enough:
            less and more or equal)
        Next step is to see how many elements we have in each group:
            if k <= L, where L is size of left, than we can be sure that we need to look into the left part.
            If k > L + M, where M is size of mid group, than we can be sure, that we need to look into the right part.
        Finally, if none of these two condition holds, we need to look in the mid part,
            but because all elements there are equal, we can immedietly return mid[0].
        Complexity: time complexity is O(n) in average, O(n^2) in worst case because on each time we reduce searching range approximately 2 times.
        This is not strict proof, for more details you can do some googling. Space complexity is O(n) as well.
        """
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
