class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = float(n)
        while n >= 1:
            if n == 1:
                return True
            n = n/4
        
        return False