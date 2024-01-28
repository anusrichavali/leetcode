class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        map = {}
        alphabet = string.ascii_uppercase
        i = 1
        while i < 27:
            map[alphabet[i - 1]] = i
            i = i + 1
        
        ctr = 1
        value = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            value = value + (ctr * map.get(columnTitle[i]))
            ctr = ctr * 26
        
        return value