class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def dfs(i, tmp):
            if i == n:
                res.append(tmp)
                return
            
            dfs(i+1, tmp)
            dfs(i+1, tmp+[nums[i]])
        dfs(0, [])
        return res
