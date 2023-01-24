class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def search():
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < 0:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        zero_i = search()
        if zero_i < 0:
            zero_i += 1
        elif zero_i >= n:
            zero_i -= 1
        neg, pos = zero_i - 1, zero_i
        res = [0] * n
        i = 0
        while neg >= 0 and pos < n:
            if nums[neg]**2 < nums[pos]**2:
                res[i] = nums[neg]**2
                neg -= 1
            else:
                res[i] = nums[pos]**2
                pos += 1
            i += 1
        while neg >= 0:
            res[i] = nums[neg]**2
            neg -= 1
            i += 1
        while pos < n:
            res[i] = nums[pos]**2
            pos += 1
            i += 1
        return res
