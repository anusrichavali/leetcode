class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        ct = 0
        for i in patterns:
            if i in word:
                ct += 1
        return ct