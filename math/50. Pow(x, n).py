class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        if n < 0:
            return self.myPow(1 / x, -n)

        if n % 2 == 1:
            # k 是奇数
            return x * self.myPow(x, n - 1)
        else:
            # k 是偶数
            sub = self.myPow(x, n // 2)
            return sub * sub