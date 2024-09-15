class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        This problem essentially asks the longest contiguous subarray with the maximum value
        Note we can't use two-pointer sliding window because we cannot undo bitwise AND
        """
        longest = 0
        current_len = 0
        max_val = 0 # min value in nums is 1, so set max_val to zero

        for num in nums:
            if num > max_val: # meet higher value, restart counting from current element
                max_val = num
                current_len = 1
                longest = 1

            elif num == max_val:
                current_len += 1
            else:
                current_len = 0 # if not set to zero when meeting smaller element, the case nums = [5,5,3,5] will fail
                # because we continue counting the third 5 as consecutive with prior two 5s even there's a lower value 3 that interrupts
                # the array

            longest = max(longest, current_len)
        return longest
