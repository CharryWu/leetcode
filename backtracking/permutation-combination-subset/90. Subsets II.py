class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            # All subset that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)

            # All subset that does not include nums[i]
            subset.pop()
            # since array is sorted, skip all duplicates
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1

            backtrack(i+1, subset)
        backtrack(0, [])
        return res
