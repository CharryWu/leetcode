
def minSumDistancesToWarehouses(nums):
    nums.sort()
    best_split = 0
    max_diff = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > max_diff:
            best_split = i
            max_diff = nums[i] - nums[i - 1]

    first_half = nums[:best_split]
    second_half = nums[best_split:]

    first_centroid = round(sum(first_half) / len(first_half))
    second_centroid = round(sum(second_half) / len(second_half))

    total_dist = 0
    for num in nums:
        total_dist += min(abs(num - first_centroid), abs(num - second_centroid))
    return total_dist

print(minSumDistancesToWarehouses([0, 1, 2,2,2,2,4,4,8,9,9,10,10,11,13,14]))
