from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return

            if i >= len(nums) or total > target:
                return

            path.append(nums[i])
            dfs(i, path, total+nums[i])
            path.pop()
            dfs(i+1, path, total)


        dfs(0, [], 0)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            elif total > target or i >= n:
                return

            else:
                for j in range(i, n):
                    path.append(candidates[j])
                    backtrack(j, path, total+candidates[j])
                    path.pop()

        backtrack(0, [], 0)
        return res

def combination_sum_neg(candidates, target):
    candidates.sort()
    n = len(candidates)
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return

        for i in range(start, n):
            if i > start and candidates[i] == candidates[i-1]:
                continue

            if candidates[i] > 0 and candidates[i] > target:
                break

            if candidates[i] < 0 and candidates[i] < target:
                continue

            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()

    result = []
    backtrack(0, target, [])
    return result

# Example usage
candidates = [2, -3, 7, 5, -2]
target = 5
print(combination_sum_neg(candidates, target))
