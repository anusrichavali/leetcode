class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = []

        def recursion(i, combo, t):
            if t == target:
                copy = list(combo)
                solutions.append(copy)
                return
            if i >= len(candidates) or t > target:
                return

            combo.append(candidates[i])
            recursion(i, combo, t + candidates[i])
            combo.pop()
            recursion(i + 1, combo, t)

        recursion(0, [], 0)
        return solutions