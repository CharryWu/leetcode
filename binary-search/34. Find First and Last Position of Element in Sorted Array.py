class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        foundL, foundR = -1, -1
        
        left, right = 0, n # search left pos
        while left < right:
            mid = (left+right) // 2
            # 找到 target 时不要立即返回，而是缩小「搜索区间」的上界 right，
            # 在区间 [left, mid) 中继续搜索，即不断向左收缩，达到锁定左侧边界的目的
            if target == nums[mid]:
                right = mid
            
            elif target < nums[mid]:
                right = mid
            
            elif target > nums[mid]:
                left = mid+1
            
        if left < n and nums[left] == target:
            foundL = left
        
        
        left, right = 0, n # search right pos
        while left < right:
            mid = (left+right) // 2
            if target == nums[mid]:
                # 当 nums[mid] == target 时，不要立即返回，
                # 而是增大「搜索区间」的左边界 left，使得区间不断向右靠拢，达到锁定右侧边界的目的
                left = mid+1
            
            elif target < nums[mid]:
                right = mid
            
            elif target > nums[mid]:
                left = mid+1
        
        # 因为我们对 left 的更新必须是 left = mid + 1，就是说 while 循环结束时，nums[left] 一定不等于 target 了，而 nums[left-1] 可能是 target。
        # 至于为什么 left 的更新必须是 left = mid + 1，当然是为了把 nums[mid] 排除出搜索区间，这里就不再赘述。
        if right-1 >= 0 and nums[right-1] == target:
            foundR = right-1
        
        return [foundL, foundR]