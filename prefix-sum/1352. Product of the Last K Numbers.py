class ProductOfNumbers:

    def __init__(self):
        self.presum = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.presum = [1]
        else:
            self.presum.append(num * self.presum[-1])

    def getProduct(self, k: int) -> int:
        if k >= len(self.presum):
            return 0
        return self.presum[-1] // self.presum[-k-1]

