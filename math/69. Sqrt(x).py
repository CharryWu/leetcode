class Solution:
    def mySqrt(self, x: int) -> int:
        """
        If x < 2, return x.
        Set the left boundary to 2, and the right boundary to x / 2.

        While left <= right:
        - Take num = (left + right) / 2 as a guess. Compute num * num and compare it with x:
        - If num * num > x, move the right boundary right = pivot -1
        - Else, if num * num < x, move the left boundary left = pivot + 1
        - Otherwise num * num == x, the integer square root is here, let's return it
        """
        if x == 0 or x == 1:
            return x

        lo, hi = 1, x//2
        ans = 0

        while lo <= hi:
            mid = (lo+hi) // 2
            mid_guess = mid ** 2
            if mid_guess == x:
                return mid
            elif x < mid_guess:
                hi = mid-1
            elif x > mid_guess:
                lo = mid+1
        
        return lo-1