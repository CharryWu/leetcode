class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        remainder_class = {} # remainder => (freq_counter, min_value)
        maxval = 0
        for num in nums:
            div, mod = divmod(num, space)
            if mod not in remainder_class:
                remainder_class[mod] = (1, num)
            else:
                remainder_class[mod] = (remainder_class[mod][0]+1, min(remainder_class[mod][1], num))

            maxval = max(maxval, remainder_class[mod][0])

        res = float('inf')
        for freq, minval in remainder_class.values():
            if freq == maxval:
                res = min(res, minval)
        return res
