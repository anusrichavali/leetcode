class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        s2 = ""
        while i < len(s):
            if s[i] == 'i':
                s2 = s2[::-1]
            else:
                s2 = s2 + s[i]
            i = i + 1

        return s2