class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []
        visited = set()

        def traverse():
            if len(path) == n:
                res.append(list(path))
            for j in range(n):
                if nums[j] in visited:
                    continue
                path.append(nums[j])
                visited.add(nums[j])
                traverse()
                path.pop()
                visited.remove(nums[j])
        
        traverse()
        return res


    def permuteSwap(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []

        def traverse(i):
            if i == n:
                res.append(list(path))
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                path.append(nums[i])
                traverse(i+1)
                path.pop()
                nums[i], nums[j] = nums[j], nums[i]
        
        traverse(0)
        return res