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