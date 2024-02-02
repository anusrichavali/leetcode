class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s2 = ""
        for i in s.split(' '):
            s2 = s2 + i[::-1] + ' '

        return s2.strip()
        