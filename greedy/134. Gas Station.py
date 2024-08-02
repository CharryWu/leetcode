class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Because we can freely choose the starting position, there's guarantee
        # to be one solution, if total sum of cost < total sum of gas
        # we can always pick one starting point that has most remaining gas that
        # allows it to go next
        if sum(gas) < sum(cost):
            return -1

        # there's exactly one solution, we're going to find it
        # If car starts at A and can not reach B. Any station between A and B
        # can not reach B.(B is the first station that A can not reach.)
        # If the total number of gas is bigger than the total number of cost. There must be a solution.
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1

        return res
