class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        l = list(allowed)
        count = 0
        for i in words:
            true = 0
            for j in i:
                if j not in l:
                    true = 1
            if true == 0:
                count = count + 1
        
        return count
        