class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1

        while i < j:
            cursum = numbers[i] + numbers[j]

            if cursum > target:
                j -= 1
            elif cursum < target:
                i += 1
            else:
                return [i+1, j+1]
