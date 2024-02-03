class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch in word:
            word = word[0: word.index(ch) + 1][::-1] + word[word.index(ch) + 1:len(word)]
        return word
        