class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(nums, start, end):
            """
            仅计算前闭后开区间 [start,end) 的最优结果
            """
            prev_sum = 0
            prev_prev_sum = 0
            cur_sum = 0
            max_sum = 0
            for i in range(start, end):
                cur = nums[i]
                prev_prev_sum = prev_sum
                prev_sum = cur_sum
                cur_sum = max(prev_sum, cur+prev_prev_sum)
                max_sum = max(max_sum, cur_sum)
            return max_sum

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(robRange(nums, 0, n-1), robRange(nums, 1, n))