class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        found = 0
        news, newe = newInterval
        for curs, cure in intervals:
            if news <= curs:
                break
            found += 1

        intervals.insert(found, newInterval)
        i = 0
        while i < len(intervals):
            if i < len(intervals)-1 and intervals[i][1] >= intervals[i+1][0]:
                nexts, nexte = intervals.pop(i+1)
                intervals[i][0], intervals[i][1] = min(nexts, intervals[i][0]), max(nexte, intervals[i][1])
            else:
                i += 1

        return intervals


