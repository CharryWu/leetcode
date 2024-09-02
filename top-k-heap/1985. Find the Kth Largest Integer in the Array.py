import random
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(lambda x: int(x), nums))
        # n = len(nums)

        def searchK(arr, k):
            if not arr:
                return
            pivot = random.choice(arr)
            left, mid, right = [], [], []
            for num in arr:
                if num > pivot:
                    left.append(num)
                elif num == pivot:
                    mid.append(num)
                else:
                    right.append(num)

            L, M = len(left), len(mid)

            if k <= L:
                return searchK(left, k)
            elif k > L+M:
                return searchK(right, k-L-M)
            else:
                return mid[0]

        return str(searchK(nums, k))
