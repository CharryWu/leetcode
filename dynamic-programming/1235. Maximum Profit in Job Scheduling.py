class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(endTime, startTime, profit))
        jobs.sort()
        n = len(jobs)
        # p(i) = largest index j < i such that job j is compatible with i
        prev = [-1] * n

        # compute prev array
        for i in range(n):
            start_i = jobs[i][1]
            for j in range(i-1, -1, -1):
                if jobs[j][0] <= start_i:  # compatible
                    prev[i] = j
                    break

        OPT = [0] * n  # OPT[i] is value of optimal solution for jobs 1..i
        for i in range(n):
            last_OPT = OPT[i-1] if i > 0 else 0
            OPT[i] = max(jobs[i][2] + OPT[prev[i]], last_OPT)

        return OPT[-1]
