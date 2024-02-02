class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(string.ascii_lowercase)
        new = ""
        for i in range(len(s)):
            if i%2 == 0:
                new = new + s[i]
            else:
                index = l.index(s[i-1])
                new = new + l[int(s[i]) + index]
        
        return new