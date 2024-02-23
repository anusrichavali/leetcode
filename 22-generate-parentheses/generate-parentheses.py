class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        result = []

        def generate(openCount, closeCount):
            if openCount == closeCount == n:
                result.append(''.join(stack))
                return
            
            if openCount < n:
                stack.append('(')
                generate(openCount + 1, closeCount)
                stack.pop()

            if closeCount < openCount:
                stack.append(')')
                generate(openCount, closeCount + 1)
                stack.pop()
        
        generate(0, 0)
        return result
        