class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        """
        O(n) time complexity, n = len(nums)
        """
        n = len(nums)
        diff_count = 0
        for i in range(1, n):
            diff_count = nums[i] - nums[i-1] - 1
            if (diff_count >= k):
                return nums[i-1]+k
            k -= diff_count
        return nums[n-1]+k

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