class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        seen = {0: -1}
        res = 0
        parity = 0
        for j, c in enumerate(nums):
            if c == 0:
                parity -= 1
            else:
                parity += 1
            if parity not in seen:
                seen[parity] = j
            else:
                res = max(res, j-seen[parity])
        return res
