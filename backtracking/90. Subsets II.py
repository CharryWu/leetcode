class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        path = []
        def backtrack(i):
            res.append(list(path))
            
            for next_idx in range(i, n): # consider all later elements in nums
                candidate = nums[next_idx]
                if next_idx > i and candidate == nums[next_idx-1]:
                    continue
                path.append(candidate)
                backtrack(next_idx+1) # 
                path.pop()
        backtrack(0)
        return res
