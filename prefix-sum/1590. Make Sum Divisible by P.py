class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_mod = sum(nums) % p
        prefix = 0
        n = len(nums)
        mod_seen = {} # idx of last seen
        mod_seen[0] = -1
        res = float('inf')
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            last_mod = (prefix-total_mod) % p # 注意这里需要先update last_mod，因为我们需要求的是最短区间。如果求最长区间，就在循环最后update mod
            mod_seen[prefix] = i
            if last_mod in mod_seen:
                res = min(res, i - mod_seen[last_mod])
        
        if res >= n:
            return -1
        return res
##
# [1,2,2,4,5], p = 5, total = 14, total_mod = 4
# [1,2,0,4,4] -- prefix arr

