class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = { 0:1 }
        prefix = 0
        res = 0
        for i, num in enumerate(nums):
            prefix += num
            # 注意这里的顺序，需要先更新 res 再更新 seen。
            # 不然如果出现 [1,0,0,0] k = 0 会导致重复计算次数
            # seen[prefix]是第 i+1 位数及之后数用的，不是给第 i 位数用的
            if prefix - k in seen:
                res += seen[prefix-k]
            if prefix not in seen:
                seen[prefix] = 1
            else:
                seen[prefix] += 1
            
        return res
