class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        """
        Always start handling from the two ends of the parabola. 
        The difference is when a > 0, they are larger at two ends, when a < 0, they are smaller at two ends. 
        So when a > 0, we just start to fill out the result array from end to beginning, 
        in other case, we start filling out it from start to the end of result array.
        """
        mid = -b/(2*a)
        n = len(nums)
        l, r = 0, n-1
        res = []
        if a == 0:
            for num in nums:
                res.append(b*num+c)
            return res if b >= 0 else res[::-1]
                
        while l <= r:
            if abs(nums[l]-mid) > abs(nums[r]-mid):
                res.append(a*nums[l]**2+b*nums[l]+c)
                l += 1
            else:
                res.append(a*nums[r]**2+b*nums[r]+c)
                r -= 1

        return res[::-1] if a > 0 else res
