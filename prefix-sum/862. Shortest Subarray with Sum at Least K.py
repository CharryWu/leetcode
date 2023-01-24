from collections import deque
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        Calculate prefix sum B of list A.
        B[j] - B[i] represents the sum of subarray A[i] ~ A[j-1]
        Deque d will keep indexes of increasing B[i].
        For every B[i], we will compare B[i] - B[d[0]] with K.

        Every index will be pushed exactly once.
        Every index will be popped at most once.
        """
        d = deque([[0, 0]]) # 单调队列保存 (idx, idx 之前的 prefixsum)。idx 是升序的
        res, prefix = float('inf'), 0
        for i, a in enumerate(A):
            prefix += a
            while d and prefix - d[0][1] >= K: # 符合条件的之前的 idx 尽可能从队列前端 pop 出来，取最短
                res = min(res, i + 1 - d.popleft()[0])

            # If B[i] <= B[d.back()] and moreover we already know that i > d.back(), it means that compared with d.back(),
            # For a future i, B[i]..future[i] can help us make the subarray length shorter and sum bigger, when compared to B[d.back()]..future[i].
            # So no need to keep d.back() in our deque.

            # More detailed on this, we always add at the LAST position
            # B[d.back] <- B[i] <- ... <- B[future id]
            # B[future id] - B[d.back()] >= k && B[d.back()] >= B[i]
            # B[future id] - B[i] >= k too
            # so no need to keep B[d.back()]
            while d and prefix <= d[-1][1]: # 保持单调队列的上升。将队列后端不符合条件的也pop出来
                d.pop()
            d.append([i + 1, prefix])
        return res if res < float('inf') else -1


"""py
# 官方解法
from collections import deque
class Solution(object):
    def shortestSubarray(self, A, K):
        n = len(A)
        
        presums = [0] * (n+1)
        s = 0
        for i in range(1, n+1):
            s += A[i-1]
            presums[i] = s

        #Want smallest y-x with Py - Px >= K
        presum_idx = 0
        ans = n+1 # n+1 is impossible
        monoq = deque() # opt(y) candidates, represented as indices of P
        while presum_idx < n+1:
            next_presum = presums[presum_idx]

            # If presums[presum_idx] <= presums[monoq.back()],
            # For a future id, subarray [presum_idx, future id] has bigger sum and shorter length, when compared [monoq.back(), future id].
            while monoq and next_presum <= presums[monoq[-1]]:
                monoq.pop() # no need to keep d.back() in our deque, if presums[future id] - presums[presum_idx] > presums[future id] - presums[monoq.back()]
            
            while monoq and next_presum - presums[monoq[0]] >= K: # 满足条件，取下一个candidate
                ans = min(ans, presum_idx-monoq[0])
                monoq.popleft()

            monoq.append(presum_idx)
            presum_idx += 1

        return ans if ans < n+1 else -1
"""

