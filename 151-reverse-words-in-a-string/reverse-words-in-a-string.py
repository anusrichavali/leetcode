class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr = ""
        words = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if curr:
                    words.append(curr)
                    curr = ''
            else:
                curr = s[i] + curr
        if curr:
            words.append(curr)
        return " ".join(words)        