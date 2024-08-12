def getMaxConsecutiveON(server_states, k):
    # write your code here
    # [-3,1,-1] k
    # sliding window
    lst = []
    cur = 0
    curCh = server_states[0]
    for ch in server_states:
        if ch == curCh:
            cur += 1
        else:
            lst.append((-1 if curCh == '0' else 1) * cur)
            curCh = ch
            cur = 1
    lst.append((-1 if curCh == '0' else 1) * cur)
    left = 0
    negative = 0
    total_sum = 0
    max_sum = 0
    for right in range(len(lst)):
        num = lst[right]
        if num < 0:
            negative += 1
        total_sum += abs(num)
        while negative > k:
            num_left = lst[left]
            left += 1
            if num_left < 0:
                negative -= 1
            total_sum -= abs(num_left)
        max_sum = max(max_sum, total_sum)
    return max_sum

# Example usage:
print(getMaxConsecutiveON("10101", 1)) # 3

print(getMaxConsecutiveON("00010", 1)) # 4
print(getMaxConsecutiveON("1001", 2)) # 4
print(getMaxConsecutiveON("11101010110011", 2)) # 8
