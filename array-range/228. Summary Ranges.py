class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        if n == 0:
            return []
        def generateRange(l, r):
            if l > r:
                return ''
            if l == r:
                return str(l)
            else:
                return f'{l}->{r}'
        left = 0
        for i in range(1, n):
            if nums[i] == nums[i-1]+1:
                continue
            else:
                res.append(generateRange(nums[left], nums[i-1]))
                left = i
        
        res.append(generateRange(nums[left], nums[n-1]))
        return res