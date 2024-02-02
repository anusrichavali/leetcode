class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ct = 0
        max = 0
        for i in s:
            if i == '(':
                ct = ct + 1
            elif i == ')':
                ct = ct - 1
            
            if ct > max:
                max = ct
        
        return max