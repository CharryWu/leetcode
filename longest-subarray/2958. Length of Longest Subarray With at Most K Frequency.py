from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter()
        res = 1
        l = 0
        for r in range(n):
            freq[nums[r]] += 1
            while freq[nums[r]] > k:
                # print(nums[r], freq[nums[r]])
                freq[nums[l]] -= 1 # 注意这里顺序不能反过来
                l += 1
            res = max(res, r-l+1)
        return res
