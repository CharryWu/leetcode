def getMaxRequest(bandwidth, request, total_bandwidth):
    n = len(bandwidth)
    dp = [0] * (total_bandwidth + 1)
    for i in range(n):  # select i-th request
        # calc bandwidth that serves max request
        for b in range(total_bandwidth, bandwidth[i] - 1, -1):
            dp[b] = max(dp[b], dp[b - bandwidth[i]] + request[i])
    return dp[total_bandwidth]


assert getMaxRequest(
    [200, 100, 350, 50, 100],
    [270, 142, 450, 124, 189],
    500
) == 763

assert getMaxRequest(
    [100, 500, 80, 25, 400],
    [100, 1000, 120, 110, 100],
    200
) == 230


def getMessageStatus(timestamps, messages, k):
    history = {}
    res = []
    for ts, msg in zip(timestamps, messages):
        if msg not in history:
            history[msg] = [ts]
            res.append("true")
        else:
            if history[msg][-1] + k > ts:
                res.append("false")
            else:
                res.append("true")
            history[msg].append(ts)
    return res


assert getMessageStatus(
    [1, 1, 1, 11],
    ["messsage-2", "messsage-2", "messsage-3", "messsage-2"],
    5
) == ["true", "false", "true", "true"]


MOD = 10**9+7
def maximumEfficiency(memory):
    n = len(memory)
    for i in range(n//2):
        ni = n - i
        m1, m2 = memory[i], memory[ni-1]
        memory[i], memory[ni-1] = min(m1, m2), max(m1, m2)
    return sum([memory[i]*(i+1) for i in range(n)]) % MOD

assert maximumEfficiency(
    [2,4,1,3]
) == 28

assert maximumEfficiency(
    [5,4,1,5,3,2]
) == 81


