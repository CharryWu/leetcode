class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        let's look between adjacent events, with duration time - prev_time.
        If we started a function, and we have a function in the background,
        then it was running during this time.

        Otherwise, we ended the function that is most recent in our stack
        """
        res = [0] * n
        prevtime = 0
        stack = []
        for log in logs:
            funcid, startend, time = log.split(':')
            funcid = int(funcid)
            time = int(time)

            if startend == "start":
                if stack:
                    res[stack[-1]] += time - prevtime
                stack.append(funcid)
                prevtime = time
            else:
                res[stack.pop()] += time + 1 -prevtime
                prevtime = time+1

        return res

