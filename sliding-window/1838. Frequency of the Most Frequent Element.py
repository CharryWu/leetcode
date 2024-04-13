class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sliding window, j is the new element to consider
        nums.sort() # sort so that elements closest but smaller to j will be on the left side of j, turning this problem into sliding window problem
        n = len(nums)
        i = 0
        s = 0
        res = 0
        for j in range(n):
            s += nums[j]
            potential_sum = nums[j] * (j-i+1) # make all elements inside [i, j] -> nums[j]
            if s + k < potential_sum:
                s -= nums[i]
                i += 1
            else:
                res = max(res, j-i+1)
        return res
"""
the final i, j is not necessarily the correct window in the end, but j-i+1 is still the correct answer.
why?
using [1,2,3,4,5, 100] and k = 3 as an example, the largest window size is 3 and the correct windows include [1,2,3] or [2,3,4] or [3,4,5].
when j reaches the time 100, i points to 3, of course [3,4,5,100] is not a valid window, so i is updated to point to 4. Yet that is still not the correct window because [4,5,100] cannot be made the same using only 3 operations.
However, this does not change the fact that window size 3 occurred before and remain the correct max window size.

Then the question becomes: can this solution recover from a mistaken window in the middle?
for example, k = 6 and the array is [1,3,5,7, 100,101,102,103]
1,3,5,7 are scanned, i points to item 3, so the window size so far is 3
when item 100 is reached, the condition is strongly violated even when i is updated to point to item 5, maintaining the window size to be 3.
when item 101 is reached, the condition is still violated even when i is updated to point to item 7, window size remain to be 3
when item 102 is reached, the condition is met when i is updated to point to item 100, window size remain to be 3
when item 103 is reached, the condition is still met so i remain pointing to item 100, window size increases to be 4.

We can see that the window can be incorrectly large during some portion of the array; but every time it expands, it is valid; otherwise, it will only remain its size, not increase.
Therefore, it can correctly compute the the largest window size.
"""


"""
Frequency of the Most Frequent Element
Longest Subarray of 1's After Deleting One Element
Constrained Subsequence Sum
Number of Substrings Containing All Three Characters
Count Number of Nice Subarrays
Replace the Substring for Balanced String
Max Consecutive Ones III
Binary Subarrays With Sum
Subarrays with K Different Integers
Fruit Into Baskets
Shortest Subarray with Sum at Least K
Minimum Size Subarray Sum
"""
