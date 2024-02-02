class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        spl = s.split(" ")
        return ' '.join(spl[0: k])