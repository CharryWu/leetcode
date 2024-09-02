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
        Complexity: time complexity is O(n) in average, because on each time we reduce searching range approximately 2 times.
        This is not strict proof, for more details you can do some googling. Space complexity is O(n) as well.
        """
        if not nums: return
        pivot = random.choice(nums)
        left, mid, right = [], [], []
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
