class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        output = [0] * len(temperatures)
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][1]:
                current = stack.pop()
                output[current[0]] = index - current[0]
            stack.append([index, value])
        return output
        