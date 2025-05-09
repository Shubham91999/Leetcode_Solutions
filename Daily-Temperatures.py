class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. Brute Force - Nested Loops
        # n = len(temperatures)
        # days = [0] * n
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             days[i] = j - i
        #             break
        # return days

        # 2. Monotonic Stack
        res = [0] * len(temperatures)  # Store days required
        stack = []   # Pairs -> [temp, index]

        for i, t in enumerate(temperatures): # For every temperature
            while stack and t > stack[-1][0]:  # If stack present and current temp is higher than top's temp
                stackT, stackInd = stack.pop()  # Pop top, as we found higher temp for it
                res[stackInd] = (i - stackInd)  # Adding days required in res
            stack.append([t, i])  # Adding every pair in stack
        return res

