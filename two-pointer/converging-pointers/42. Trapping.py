# No two pointer, use maxLeft[] and maxRight[] array
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        DP solution
        Use the formula: min(maxL,maxR)-height[i] at every single position i
        to determine the water that can be trapped
        L, R is the max height we've seen so far during iteration
        if formula evaluates to negative value, trap zero value
        """
        n = len(height)
        if n == 0:
            return 0

        maxLeft = [0] * n
        maxRight = [0] * n

        for i in range(n):
            if i > 0:
                # be caution here, we're recording the previous value at i-1
                maxLeft[i] = max(maxLeft[i-1], height[i-1])
                # be caution here, we're recording the previous value at n-i
                maxRight[n-i-1] = max(maxRight[n-i], height[n-i])
        print(maxLeft, maxRight)
        res = 0
        for i in range(n):
            ll = min(maxLeft[i], maxRight[i])
            res += max(0, ll - height[i])
        return res

# Use two converging pointer, moving to center


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        DP solution
        Use the formula: min(maxL,maxR)-height[i] at every single position i
        to determine the water that can be trapped
        L, R is the max height we've seen so far during iteration
        if formula evaluates to negative value, trap zero value
        """
        n = len(height)
        if n == 0:
            return 0

        i, j = 0, n-1
        leftMax, rightMax = height[0], height[n-1]
        res = 0

        while i < j:  # use two pointer, always move the pointer of lower height
            # height[i], height[j] always contributes 0 to result
            # bottleneck is always going to be the lower height
            if leftMax < rightMax:
                i += 1  # update index first, then compute.
                leftMax = max(leftMax, height[i])
                res += leftMax-height[i]
            else:
                j -= 1
                rightMax = max(rightMax, height[j])
                res += rightMax-height[j]

        return res
