class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def removeElement(nums, val):
            fast, slow = 0, 0
            while fast < len(nums):
                if nums[fast] != val:
                    nums[slow] = nums[fast]
                    slow += 1
            
                fast += 1
            
            return slow
    
        p = removeElement(nums, 0)
        while p < len(nums):
            nums[p] = 0
            p += 1
