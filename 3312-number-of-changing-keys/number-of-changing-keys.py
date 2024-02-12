class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2 = s.lower()
        ctChanges = 0
        prev = s2[0]
        for i in range(1, len(s2)):
            if s2[i] != prev:
                ctChanges += 1
            prev = s2[i]
        return ctChanges
        