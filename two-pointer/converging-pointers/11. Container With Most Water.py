class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Use two pointer
        """
        n = len(heights)
        i, j = 0, n-1
        res = 0

        while i < j:
            res = max(res, min(heights[i], heights[j]) * (j-i))
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] <= heights[i]:
                j -= 1
        return res
