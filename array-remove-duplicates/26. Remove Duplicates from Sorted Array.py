class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        # 不用额外空间的数组
        for i in range(len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[k] = nums[i]
                k += 1
                seen.add(nums[i])
        return k
"""
