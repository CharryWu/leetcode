class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time complexity: n! * n^2, we have n! permuntations, each permutation takes n^2 operations to create (insert n elements to n positions)
        # Space complexity: n! * n, we have n! permuntations, each permutation has length n
        if len(nums) == 0:
            return [[]]
        res = []
        perms = self.permute(nums[1:])
        # add nums[0] to every position of generated permutations

        for p in perms:
            for i in range(len(p)+1): # could insert at the end of permutation
                pc = p.copy()
                pc.insert(i, nums[0])
                res.append(pc)

        return res
