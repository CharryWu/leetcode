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
            # 由于数组内存在重复，所以需要跳过重复的元素
            if nums[l] == nums[l+1]:
                l += 1
            elif nums[r] == nums[r-1]:
                r -= 1
            elif nums[l] > nums[mid]:
                r = mid
            else:
                l = mid+1

        

        # 普通的二叉搜索
        def search(left, right):
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid+1
            if left < n and nums[left] == target:
                return left
            else:
                return -1

        # 特殊case：pivot 就是 target
        if nums[pivot] == target:
            return True
        # 数组没有被旋转，在整个数组内找
        if pivot == 0 and search(0, n-1) != -1:
            return True
        # 在数组旋转点之前找
        if target < nums[0] and search(pivot, n-1) != -1:
            return True
        # 在数组旋转点之后找
        if target >= nums[0] and search(0, pivot-1) != -1:
            return True
        return False
        
