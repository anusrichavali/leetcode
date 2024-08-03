class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        new = ""
        while i < min(len(word1), len(word2)):
            new += word1[i] + word2[i]
            i += 1
        if i < len(word1):
            new += word1[i: len(word1)]
        else:
            new += word2[i: len(word2)]
        return new
        