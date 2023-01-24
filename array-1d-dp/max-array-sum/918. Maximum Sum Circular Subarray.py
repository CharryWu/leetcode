# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
"""
I guess you know how to solve max subarray sum (without circular).
If not, you can have a reference here: 53. Maximum Subarray

There are two case.
Case 1. The first is that the subarray take only a middle part, and we know how to find the max subarray sum.
Case2. The second is that the subarray take a part of head array and a part of tail array.


Intuition: the max subarray circular sum equals to
max(the max subarray sum, the total sum - the min subarray sum)

Corner case
Just one to pay attention:
If all numbers are negative, maxSum = max(A) and minSum = sum(A).
In this case, max(maxSum, total - minSum) = 0, which means the sum of an empty subarray.
According to the description, We need to return the max(A), instead of sum of am empty subarray.
So we return the maxSum to handle this corner case.

"""
class Solution:
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
