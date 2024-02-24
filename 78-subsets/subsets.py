class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        subset = []

        def recursion(i):
            if i >= len(nums):
                copy = list(subset)
                solution.append(copy)
                return
            
            subset.append(nums[i])
            recursion(i + 1)

            subset.pop()
            recursion(i + 1)

        recursion(0)
        return solution