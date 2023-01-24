"""
为什么 while 循环的条件中是 <=，而不是 <？

答：因为初始化 right 的赋值是 nums.length - 1，即最后一个元素的索引，而不是 nums.length。

这二者可能出现在不同功能的二分查找中，区别是：前者相当于两端都闭区间 [left, right]，后者相当于左闭右开区间 [left, right)，因为索引大小为 nums.length 是越界的。
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right-left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]
                left = mid + 1
            else: # target < nums[mid]
                right = mid
        return -1
