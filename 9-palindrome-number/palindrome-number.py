class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        og = x
        rev = 0
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x /= 10
        return og == rev