class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alpha = list(string.ascii_lowercase)
        for i in sentence:
            if i in alpha:
                alpha.pop(alpha.index(i))
        
        return len(alpha) == 0