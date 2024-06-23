class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Turn original input into a set to detect if the prev number occured
        """
        num_set = set(nums) # turn list into set for fast query
        res = 0

        for num in nums:
            if num-1 not in num_set: # found start of new sequence, doesn't have prev
                length = 1
                while num+length in num_set: # go as far as we can to find the end of consecutive sequence
                    length += 1
                res = max(res, length)
        return res
