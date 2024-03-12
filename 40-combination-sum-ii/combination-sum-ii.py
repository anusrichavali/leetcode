class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''
        problem requires backtracking -- find all unique combos
        decision: add a value only if the sum <= target
        base case: if sum of the subset equals target and subset not in result, append to solution
        Logic: Choice - whether or not to add a value as long as the sum less than target
        solution = []
        Constraint: has to be less than target
        '''
        solution = []
        candidates.sort()

        def makeSubset(pos, curr_set):
            if sum(curr_set) == target and curr_set not in solution:
                solution.append(curr_set[::])
                return
            if sum(curr_set) > target:
                return
            if pos >= len(candidates):
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr_set.append(candidates[i])
                makeSubset(i + 1, curr_set)
                curr_set.pop()
                prev = candidates[i]
        
        makeSubset(0, [])
        return solution
