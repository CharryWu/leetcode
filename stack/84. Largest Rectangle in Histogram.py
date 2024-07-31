class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic stack of increasing heights. If encounter a smaller height
        # remove all most recent smaller heights and remove from stack
        res = 0
        stack = [] # index, height

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # current height lower than stack top, pop stack
                previndex, prevheight = stack.pop()
                res = max(res, prevheight * (i-previndex)) # the height of rectangle at previndex extends all the way to current index, i
                start = previndex # since current height h is smaller than stack top prevheight, current height can extend all the way back to previndex
            stack.append((start, h))

        # calculate remaining heights in stack
        for i, h in stack:
            # the width at i extend all the way to end of histogram
            res = max(res, h * (len(heights) - i))
        return res
