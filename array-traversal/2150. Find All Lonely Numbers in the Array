class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        res = []
        if n == 1:
            return nums
        for i in range(n):
            if i == 0 and nums[1] > nums[0]+1:
                res.append(nums[0])
                continue
            if i == n-1 and nums[i-1] < nums[i]-1:
                res.append(nums[i])
                continue
            if nums[i-1] + 1 < nums[i] < nums[i+1] -1:
                res.append(nums[i])
        return res
