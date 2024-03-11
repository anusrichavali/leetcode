class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        opening = []
        closing = []
        for i in s:
            if i == '(':
                opening.append('(')
            else:
                if opening:
                    opening.pop()
                else:
                    closing.append(')')
        return len(opening) + len(closing)
        