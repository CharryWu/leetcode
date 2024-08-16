def getMaximumSum(health, serverType, k):
    from collections import defaultdict

    # Step 1: Accumulate the health sums per server type
    health_by_type = defaultdict(int)
    for h, t in zip(health, serverType):
        health_by_type[t] += h
    print(health_by_type)

    # Step 2: Sort the accumulated health values in descending order
    sorted_health_values = sorted(health_by_type.values(), reverse=True)

    # Step 3: Select the top k health values and return their sum
    return sum(sorted_health_values[:k])

# Example usage:
health = [4, 5, 5, 6]
serverType = [1, 2, 1, 2]
k = 1
print(getMaximumSum(health, serverType, k))  # Output should be 11


health = [4, 2, 3, 5, 10]
serverType = [3, 3, 1, 2, 5]
k = 2
print(getMaximumSum(health, serverType, k))  # Output should be 20


