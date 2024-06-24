class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # curTemp > top of stack, found a warmer temperature
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t, i])

        return res
