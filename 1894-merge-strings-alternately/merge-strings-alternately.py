class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        total = ""
        for i in range(min(len(word1), len(word2))):
            total += word1[i] + word2[i]
        if len(word2) > len(word1):
            total += word2[len(word1):]
        else:
            total += word1[len(word2):]
        return total