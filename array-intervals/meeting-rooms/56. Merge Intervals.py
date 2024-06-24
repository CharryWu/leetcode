class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # do normal sort of based on start value
        # don't care about end value

        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if lastEnd >= start: # mergeable
                output[-1][1] = max(end, lastEnd) # take max of (curend, prevend). Example: [1,5], [2,4]
            else:
                output.append([start, end])
        return output
