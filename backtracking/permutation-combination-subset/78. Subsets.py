class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []

        def dfs(i): # current index in decision tree
            if i >= len(nums): # out of bounds, terminate condition
                res.append(stack.copy())
                return

            # decision to include nums[i]
            stack.append(nums[i])
            dfs(i+1)

            # decision to not include nums[i]
            stack.pop()
            dfs(i+1) # have a different subset

        dfs(0)
        return res
