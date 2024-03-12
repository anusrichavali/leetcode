class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        #All possible indicates backtracking
        #At any given position, add the char at the currrent pos
        #if is palindrome, add and return
        #else, backtrack by returning empty
        solution = []
        partition = []

        def isPalindrome(s, i, j):
            return s[i: j + 1] == s[i: j + 1][::-1]

        def splitStr(i):
            if i >= len(s):
                solution.append(partition[::])
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    partition.append(s[i:j + 1])
                    splitStr(j + 1)
                    partition.pop()

        splitStr(0)
        return solution