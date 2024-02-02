class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev = s[::-1]
        new = ""
        a = string.ascii_lowercase
        for i in range(len(s)):
            if s[i] != rev[i]:
                rep = min(a.index(s[i]), a.index(rev[i]))
                new = new + a[rep]
            else:
                new = new + s[i]
        return new
        