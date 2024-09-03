class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 1
        while i < n:
            diff = nums[i] - nums[i-1]
            if diff > k:
                return nums[i-1] + k
            else:
                k -= (diff-1)
            i += 1

        return nums[n-1] + k

"""
# Naive Approach: O(k) time complexity
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        candidate = nums[0]
        idx = 0
        while k > 0:
            if idx < n:
                if candidate == nums[idx]:
                    idx += 1
                else:
                    k -= 1
                candidate += 1
            else:
                candidate += 1
                k -= 1
        return candidate-1
"""
