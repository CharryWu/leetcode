class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot_idx = n-1
        if nums[0] > nums[n-1]:
            left, right = 0, n-1
            while left <= right:
                mid = (left+right) // 2
                if mid < n-1 and nums[mid+1] < nums[mid]:
                    pivot_idx = mid
                    break
                
                if mid == 0: # nums[mid+1] > nums[mid], 如果此时mid == 0，则pivot_idx 一定在右边
                    left = mid+1
                elif nums[0] > nums[mid]:
                    right = mid-1
                elif nums[0] < nums[mid]:
                    left = mid+1
        
        left, right = 0, n-1
        if target == nums[pivot_idx]:
            return pivot_idx
        elif target >= nums[0]:
            left, right = 0, pivot_idx
        elif target < nums[0]:
            left, right = pivot_idx + 1, n-1
        # print(left, right)
        while left <= right:
            mid = (left+right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
        return -1

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        # finding the pivot
        pivot = 0
        while l < r:
            mid = (l+r) // 2
            
            if mid < n-1 and nums[mid] > nums[mid+1]:
                pivot = mid+1
                break
            
            elif nums[l] > nums[mid]:
                r = mid
            else:
                l = mid+1
        def search(left, right):
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            if left < n and nums[left] == target:
                return left
            else:
                return -1
        
        if nums[pivot] == target:
            return pivot
        if pivot == 0:
            return search(0, n-1)
        if target < nums[0]:
            return search(pivot, n-1)
        else:
            return search(0, pivot)
        
"""