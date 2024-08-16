

# There are N buckets of apples. We would like to collect K apples from a row of continuous buckets.
#  Write a function that returns the first buckets combo that would fulfil the requirement.
#  If there is no valid buckets, return []
# Example 1:
# Apples in buckets: [2, 3, 4, 5, 6, 2, 3]
#  Apples to collect: 9
#  Buckets to collect (return value): [2, 3, 4]
# Example 2:
# Apples in buckets: [2, 3, 4, 5, 6, 2, 3]
#  Apples to collect: 7
#  Buckets to collect (return value): [3, 4]

# Input:
# First param: k, k > 0
# Second param: n integers, buckets[i] > 0

def solution(k, buckets):
    n = len(buckets)
    count = 0
    left = 0

    for right in range(n):
        count += buckets[right]
        # check if count satisfies
        if count == k:
            return buckets[left:right+1]

        while count > k: # move left pointer till count <= k
            count -= buckets[left]
            left += 1

            if count == k:
                return buckets[left:right+1]
    return []

print(solution(9, [2, 3, 4, 5, 6, 2, 3]))
print(solution(7, [2, 3, 4, 5, 6, 2, 3]))
print(solution(6, [1,2,3]))
print(solution(6, [1,2,2]))
print(solution(1, [1]))
print(solution(1, [1,2]))
print(solution(2, [1,2]))


# Second round
# How to implement a triangle down arrow CSS? Use border
# What is the box model in CSS?
# Use JS to sort a list of version number: ["1.21.0","1.2.1","1.2.0","1.1.1","1.1.0","1.0.1","1.0.0"]. The version number could contain invalid characters

# Final round (HM)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # curTemp > top of stack, found a warmer temperature
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t, i])

        return res
