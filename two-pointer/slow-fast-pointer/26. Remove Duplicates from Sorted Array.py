class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1
                