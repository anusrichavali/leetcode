class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        rev = []
        for i in words:
            rev.append(i[::-1])
        
        ct = 0
        print(rev)
        for i in words:
            if i in rev and words.index(i) != rev.index(i):
                ct = ct + 1
        return ct/2
        