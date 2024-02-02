class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev = s[::-1]
        a = string.ascii_lowercase
        for i in range(len(s)):
            if s[i] != rev[i]:
                rep = min(a.index(s[i]), a.index(rev[i]))
                s = s[0: i] + a[rep] + s[i + 1: len(s)]
        return s
        