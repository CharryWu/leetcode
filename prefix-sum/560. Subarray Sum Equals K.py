from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = Counter()
        seen[0] = 1
        prefix = 0
        res = 0
        for i, num in enumerate(nums):
            prefix += num
            if prefix - k in seen:
                res += seen[prefix-k]
            seen[prefix] += 1
        return res
