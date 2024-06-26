

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
