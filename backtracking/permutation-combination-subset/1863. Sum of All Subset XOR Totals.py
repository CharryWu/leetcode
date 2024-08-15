class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        def backtrack(path, i):
            if i == n:
                x = 0
                for num in path:
                    x ^= num
                nonlocal res
                res += x
                return

            path.append(nums[i])
            backtrack(path, i+1)
            path.pop()
            backtrack(path, i+1)
        backtrack([], 0)
        return res
