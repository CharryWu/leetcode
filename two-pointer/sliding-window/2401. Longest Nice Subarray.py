# 双指针 + 滑动窗口
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, right = 0, 1
        res = 1 # 符合题目条件 最长subarray长度
        window_bits = nums[0] # window_bits 保存当前窗口的所有数位上的 1
        
        while right < len(nums):
            # nums[r] & window_bits 如果为零，则 nums[r] 和当前窗口内任一数 AND 操作都为零，可以直接将 nums[r] 加入当前窗口；
            # 反之，则更新左指针，剔除当前窗口内的元素直到条件符合为止
            rnum = nums[right]
            ## 任何时候 window_bits 的某数位上的一个 1 都是由窗口内某一单个数贡献的，不可能出现window里面有两个数同一位均为1的情况，所以可以直接用 减法或 XOR ^= 剔除
            ## 证明：window的数都是不断地被加进来的，如果新加入的一个数 和之前另一位window里的数在同一位都是1的话，题目条件不满足，就不可能被加入window里面
            while right > left and (rnum & window_bits) != 0:
                window_bits ^= nums[left]
                left += 1
            
            res = max(res, right-left+1)

            # 注意这里的更新顺序，要先检查rnum & window_bits 确保 window_bits 已经能兼容rnum 了，再更新window_bits
            window_bits |= rnum
            right += 1

        return res

