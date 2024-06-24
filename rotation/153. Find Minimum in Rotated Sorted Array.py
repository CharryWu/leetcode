class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        detect whether mid pointer is in left portion or right portion using:
        Condition nums[mid] >= nums[l]

        if mid pointer in left portion, check left
        if mid pointer in right portion, check right
        """
        l, r = 0, len(nums)-1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]: # current portion is already sorted, minimum = nums[l]
                res = min(res, nums[l])
                break
            mid = (l+r) // 2
            res = min(res, nums[mid]) # update result with mid pointer
            if nums[mid] >= nums[l]: # >= handles edge case
                l = mid + 1
            else:
                r = mid - 1
        return res
