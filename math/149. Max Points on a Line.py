class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 0
        for i in range(n):
            x1, y1 = points[i]
            slopes = {}
            slope = 0
            currMax = 1
            for j in range(i+1, n):
                x2, y2 = points[j]

                # no need to worry about intercept bcs
                # the slope calculates from the same starting point (x1, y1) for every other x2, y2
                # no need to worry about pos/neg slope, because 
                # the slope is same for two points no matter which direction you calc from
                if x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y2-y1)/(x2-x1)
                if slope not in slopes:
                    slopes[slope] = 2
                else:
                    slopes[slope] += 1

                currMax = max(currMax, slopes[slope])

            ans = max(ans, currMax)
        return ans