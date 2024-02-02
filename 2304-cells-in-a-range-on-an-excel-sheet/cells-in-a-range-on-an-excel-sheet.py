class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = []
        first = string.ascii_uppercase.index(s[0])
        second = string.ascii_uppercase.index(s[3])
        firstInt = int(s[1])
        secondInt = int(s[4])
        for i in range(first, second + 1):
            for j in range(firstInt, secondInt + 1):
                st = string.ascii_uppercase[i] + str(j)
                l.append(st)
        return l