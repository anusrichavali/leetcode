class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        l = list(s)
        for i in t:
            if i not in l:
                return False
            else:
                l.remove(i)

        return True