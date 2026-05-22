class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_index , stack_temp = stack.pop()
                res[stack_temp] = i - stack_temp
            stack.append((t,i))
        return res