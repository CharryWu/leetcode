class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                el = nums[fast]
                # be careful of the assignment order
                nums[fast] = 0
                nums[slow] = el
                slow += 1
