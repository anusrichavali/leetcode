class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        ct_line = 0
        ct = 0
        for i in s:
            if i == '|':
                ct_line = ct_line + 1
            
            if ct_line % 2 == 0 and i == '*':
                ct = ct + 1
        
        return ct
        