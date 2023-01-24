class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefixsum = [0] * (n+1)
        s = 0
        for i, num in enumerate(nums):
            s += num
            self.prefixsum[i+1] = s

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixsum[right+1] - self.prefixsum[left]   
