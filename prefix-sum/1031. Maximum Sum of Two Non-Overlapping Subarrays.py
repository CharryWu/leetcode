class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i] + num

        def maxsum(len1, len2):
            """
            |...| arr1 | ... | arr2 | ... |
                len1^       len2^  i^
            In each iteration, we consider two arrays
            arr1 = nums[i-len2-len1:i-len2] and
            arr2 = nums[i-len2:i]

            These two arrays are used to update two sum variables, maxl and ans
            maxl is the maximum sum of ANY subarray size len1 to the left of arr2, in the range of nums[0:i-len2]
            res is the combined sum of ANY TWO non-overlapping subarrays size len1 and len2

            `maxl` is only updated when we encounter a bigger arr1 sum:
                prefix[i-len2]-prefix[i-len1-len2]
            `res` is only updated when we encounter a bigger maxl AND bigger arr2 sum:
                maxl + prefix[i] - prefix[i-len2]

            The finaly result is given by `res`. However, since firstLen and secondLen can differ,
            we run the above algorithm with different parameters
                len1 = firstLen, len2 = secondLen;
                len1 = secondLen, len2 = firstLen
            """
            maxl, ans = 0, 0
            for i in range(len1+len2, len(prefix)):
                maxl = max(maxl, prefix[i-len2]-prefix[i-len1-len2])
                ans = max(ans, maxl + prefix[i] - prefix[i-len2])
            return ans

        return max(maxsum(firstLen, secondLen), maxsum(secondLen, firstLen))
