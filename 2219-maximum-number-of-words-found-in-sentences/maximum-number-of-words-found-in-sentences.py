class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        m = 0
        for i in sentences:
            s = i.split(" ")
            if len(s) > m:
                m = len(s)
        return m
        