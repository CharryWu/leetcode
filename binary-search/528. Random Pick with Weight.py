import random
class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self):
        rand = random.random()
        cutoff = rand * self.total
        # find first element greater than or equal to cutoff
        low, high = 0, len(self.prefix)
        while low < high:
            mid = (low + high) // 2
            if cutoff > self.prefix[mid]:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
