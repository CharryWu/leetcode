class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = [0] * k
        seen[0] = 1
        prefix = 0
        res = 0
        for num in nums:
            prefix = (prefix + num) % k
            res += seen[prefix]
            seen[prefix] += 1
        
        return res
