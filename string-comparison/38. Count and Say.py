memo = {1: "1"}

def compute(prev_str):
    counts = []
    count = 1
    n = len(prev_str)
    for i in range(1, len(prev_str)):
        if prev_str[i] == prev_str[i-1]:
            count += 1
        else:
            counts.append(str(count) + prev_str[i-1])
            count = 1
    counts.append(str(count) + prev_str[n-1])
    return ''.join(counts)
    

class Solution:
    def countAndSay(self, n: int) -> str:
        for i in range(2, n+1):
            if i in memo:
                pass
            else:
                memo[i] = compute(memo[i-1])
        return memo[n]