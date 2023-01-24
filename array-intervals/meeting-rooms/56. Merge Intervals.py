class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            prev_start, prev_end = res[-1]
            if cur_start <= prev_end:
                res[-1][1] = max(prev_end, cur_end)
            else:
                res.append([cur_start, cur_end])
        
        return res