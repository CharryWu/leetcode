doubles = []
powersOfTwo = []

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        sign = 1 if dividend ^ divisor >= 0 else -1
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        doubles = []
        powersOfTwo = []
        powerOfTwo = 1
        while divisor <= dividend:
            doubles.append(divisor)
            powersOfTwo.append(powerOfTwo)
            # Prevent needless overflows from occurring...
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor # Double divisor
            powerOfTwo += powerOfTwo

        quotient = 0
        for i in reversed(range(len(doubles))):
            if doubles[i] <= dividend:
                # If it does fit, add the current powerOfTwo to the quotient.
                quotient += powersOfTwo[i]
                # Update dividend to take into account the bit we've now removed.
                dividend -= doubles[i]

        return min(quotient, MAX_INT) if sign > 0 else max(-quotient, MIN_INT)