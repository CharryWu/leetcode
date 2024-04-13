function getMaxRequests(bandwidth: number[], request: number[], total_bandwidth: number): number {
    // Write your code here
    const n = bandwidth.length
    const dp = Array(total_bandwidth+1).fill(0)
    for (let i = 0; i < n; i++) {
        for (let b = total_bandwidth; b >= bandwidth[i]; b--) {
            dp[b] = Math.max(dp[b], dp[b-bandwidth[i]] + request[i])
        }
    }
    return dp[total_bandwidth]
}


function getMessageStatus(timestamps: number[], messages: string[], k: number): string[] {
    // Write your code here
    const history: Record<string, Array<number>> = {}
    const res: string[] = []
    for (let i = 0; i < timestamps.length; i++) {
        const ts = timestamps[i]
        const msg = messages[i]

        if (! (msg in history)) {
            history[msg] = [ts]
            res.push('true')
        } else {
            let msglen = history[msg].length
            if (history[msg][msglen-1] + k > ts) {
                res.push('false')
            } else {
                res.push('true')
            }
            history[msg].push(ts)
        }
    }
    return res
}

const MOD = 10**9+7
function maximumProductSum(memory: number[]): number {
    // Write your code here
    const n = memory.length
    for (let i = 0; i < Math.floor(n / 2); i++) {
        const ni = n-i
        const m1 = memory[i]
        const m2 = memory[ni-1]
        memory[i] = Math.min(m1, m2)
        memory[ni-1] = Math.max(m1, m2)
    }

    let sum = 0
    for (let i = 0; i < n; i++) {
        sum += memory[i] * (i+1)
        sum %= MOD
    }
    return sum
}
