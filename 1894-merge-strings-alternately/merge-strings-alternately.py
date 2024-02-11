class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        merged = ""
        while i < min(len(word1), len(word2)):
            merged = merged + word1[i] + word2[i]
            i += 1
        if i < len(word1):
            merged = merged + word1[i:len(word1)]
        elif i < len(word2):
            merged = merged + word2[i:len(word2)]
        return merged



        