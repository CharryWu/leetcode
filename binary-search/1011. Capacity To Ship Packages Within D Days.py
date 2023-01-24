class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def calc_days(capacity):
            """
            Greedily fill the container ship with `capacity`. Output # of days required to ship all items in weight
            定义：当运载能力为 x 时，需要 f(x) 天运完所有货物
            f(x) 随着 x 的增加单调递减
            """
            res = 0
            i = 0
            cur = 0
            while i < n:
                if cur+weights[i] > capacity:
                    res += 1
                    cur = 0
                    continue
                else: # 尽可能多装货物
                    cur += weights[i]
                    i += 1
            if cur > 0:
                res += 1
            return res

        # 船的最小载重是多少？最大载重是多少？
        # 显然，船的最小载重应该是weights数组中元素的最大值，因为每次至少得装一件货物走，不能说装不下嘛。
        # 最大载重显然就是weights数组所有元素之和，也就是一次把所有货物都装走。
        # 这样就确定了搜索区间[left, right)
        lo_cap, hi_cap = 0, 1 # hi_cap 是开区间，所以额外加一
        for w in weights:
            lo_cap = max(lo_cap, w)
            hi_cap += w
        
        while lo_cap < hi_cap:
            mid_cap = (lo_cap+hi_cap) // 2
            mid_days = calc_days(mid_cap)
            
            if days == mid_days:
                hi_cap = mid_cap # 搜索左侧边界，则需要收缩右侧边界
            elif days < mid_days:
                lo_cap = mid_cap+1 # 需要让 f(x) 的返回值大一些
            elif days > mid_days:
                hi_cap = mid_cap # 需要让 f(x) 的返回值小一些
        return lo_cap