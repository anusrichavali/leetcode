class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        sub = 0
        for i in s:
            if i == 'L':
                l = l + 1
            else:
                r = r + 1
            
            if l == r:
                sub = sub + 1
                l = r = 0
        
        return sub
        