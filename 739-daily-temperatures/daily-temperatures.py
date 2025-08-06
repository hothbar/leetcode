class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                r[stackInd] = i - stackInd
            stack.append((t, i))
        return r