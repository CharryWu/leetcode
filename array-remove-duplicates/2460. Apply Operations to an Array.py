class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        def moveZeroes(nums: List[int]) -> None:
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

        moveZeroes(nums)
        return nums
