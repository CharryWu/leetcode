from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(path, remaining_count):
            if len(path) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(path))
                return

            for num in remaining_count: # use hashmap to avoid duplicate paths (but still allow duplicate *elements* in path)
                if remaining_count[num] > 0:
                    # add this number into the current combination
                    path.append(num)
                    remaining_count[num] -= 1
                    # continue the exploration
                    backtrack(path, remaining_count)
                    # revert the choice for the next exploration
                    path.pop()
                    remaining_count[num] += 1

        backtrack([], Counter(nums))

        return results