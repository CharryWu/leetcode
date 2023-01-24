"""
这题需要复用 阶乘后的零 这道题的解法函数 trailingZeroes。

搜索有多少个 n 满足 `trailingZeroes(https://labuladong.github.io/article/fname.html?fname=二分查找详解) 中「搜索左侧边界」和「搜索右侧边界」这两个事儿嘛？

观察题目给出的数据取值范围，n 可以在区间 [0, LONG_MAX] 中取值，寻找满足 trailingZeroes(n) == K 的左侧边界和右侧边界，相减即是答案。
"""
MAX_VALUE = 2**63-1
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailingZeroes(n: int) -> int:
            res = 0
            divisor = 5
            while divisor <= n:
                res += n // divisor
                divisor *= 5
            return res
        
        # 搜索 trailingZeroes(n) == K 的左侧边界
        def left_bound(target_zeros):
            lo, hi = 0, MAX_VALUE
            while lo < hi:
                mid = (lo+hi) // 2
                mid_zeros = trailingZeroes(mid)
                if mid_zeros < target_zeros:
                    lo = mid + 1
                elif mid_zeros > target_zeros:
                    hi = mid
                elif mid_zeros == target_zeros:
                    hi = mid
            return lo

        # 搜索 trailingZeroes(n) == K 的右侧边界
        def right_bound(target_zeros):
            lo, hi = 0, MAX_VALUE
            while lo < hi:
                mid = (lo+hi) // 2
                mid_zeros = trailingZeroes(mid)
                if mid_zeros < target_zeros:
                    lo = mid + 1
                elif mid_zeros > target_zeros:
                    hi = mid
                elif mid_zeros == target_zeros:
                    lo = mid + 1
            return hi-1
        
        left, right = left_bound(k), right_bound(k)
        return right-left+1