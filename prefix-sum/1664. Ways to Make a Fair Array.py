class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        odd_sum = [0] * n
        even_sum = [0] * n
        os = 0
        es = 0

        for i in range(n):
            os += nums[i] if i % 2 == 1 else 0
            es += nums[i] if i % 2 == 0 else 0
            odd_sum[i] = os
            even_sum[i] = es
        for i in range(n):
            even = i % 2 == 0
            prev_e = even_sum[i] - nums[i] if even else even_sum[i]
            after_e = odd_sum[n-1] - odd_sum[i]
            prev_o = odd_sum[i] - nums[i] if not even else odd_sum[i]
            after_o = even_sum[n-1] - even_sum[i]
            if prev_e + after_e == prev_o + after_o:
                count += 1
        return count
