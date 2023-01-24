class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: (x[1], x[0]))
        prevend = float('-inf')
        for start, end in intervals:
            if start >= prevend:
                prevend = end
                continue
            else:
                return False
        
        return True