class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        pivot = 0
        while l <= r:
            mid = (l+r) // 2
            if mid < n-1 and nums[mid] > nums[mid+1]:
                pivot = mid+1
                break
            elif nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
            
        return nums[pivot]
