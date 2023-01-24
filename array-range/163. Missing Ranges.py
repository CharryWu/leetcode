class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        n = len(nums)
        def generateRange(l, r):
            if l == r:
                return str(l)
            else:
                return f'{l}->{r}'
        if n == 0:
            return [generateRange(lower, upper)]
        if lower < nums[0]:
            res.append(generateRange(lower, nums[0]-1))

        for i, num in enumerate(nums):
            if i > 0 and nums[i] != nums[i-1]+1:
                res.append(generateRange(nums[i-1]+1, nums[i]-1))
        
        if upper > nums[n-1]:
            res.append(generateRange(nums[n-1]+1, upper))
        return res