class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        这题珂珂吃香蕉的速度就是自变量 x，吃完所有香蕉所需的时间就是单调函数 f(x)，target 就是吃香蕉的时间限制 H。
        f(x) = consume_all_time(x)为单调递减函数
        """
        def consume_all_time(piles, speed):
            res = 0
            for banana_count in piles:
                div, mod = divmod(banana_count, speed)
                res += div
                if mod > 0:
                    res += 1
            return res

        leftK, rightK = 1, 10**9+1 # 速度最小为1，最大可能到 10**9，因为 1 <= piles[i] <= 10**9
        while leftK < rightK:
            midK = (leftK+rightK) // 2
            mid_time = consume_all_time(piles, midK)
            if h == mid_time:
                rightK = midK
            elif h > mid_time: # consume_all_time(x)为单调递减函数，所以当 h > mid_time 需要到mid 之左寻找 H
                rightK = midK
            elif h < mid_time:
                leftK = midK+1
        
        return leftK