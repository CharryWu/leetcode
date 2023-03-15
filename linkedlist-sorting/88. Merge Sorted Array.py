# Also see https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1 # initialize i,j pointers to last element of nums1 and nums2
        k = len(nums1)-1 # write pointer to store result

        # write the result from back to front, doing it this way can prevent
        # meddling with data that's already written to the front
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
