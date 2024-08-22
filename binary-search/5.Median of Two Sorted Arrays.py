class Solution:
    """
    Find the median of two sorted arrays.

    :param nums1: The first sorted array
    :param nums2: The second sorted array
    :return: The median of two sorted arrays
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Make sure nums2 is the longer array
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2) # m < n
        total = m+n
        half = (m+n) // 2

        # search in nums1 array only
        l, r = 0, m-1
        while True:
            i = (l+r) // 2 # i is index of end of left partition, left has i+1 elements
            j = half - i - 2 # half-i-1 is number of left partitions in nums2, half-i-2 is the index of end of left partition

            # Calculate the value of the elements at the boundary of the two partitions
            left1 = nums1[i] if i >= 0 else float('-inf')
            right1 = nums1[i+1] if i+1 < m else float('inf')
            left2 = nums2[j] if j >= 0 else float('-inf')
            right2 = nums2[j+1] if j+1 < n else float('inf')

            # Check whether the current partition is correct
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    # If the total number of elements is even, return the average
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    # If the total number of elements is odd, return the smaller one
                    return min(right1, right2)

            # If the left partition is larger, move the right pointer to the left
            elif left1 > right2:
                r = i-1
            # If the left partition is smaller, move the left pointer to the right
            else:
                l = i+1
