class Solution(object):

    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        l = [""] * 10
        for i in range(0, len(rings), 2):
            l[int(rings[i + 1]) - 1] = l[int(rings[i + 1]) - 1] + rings[i]
        
        ct = 0
        for i in l:
            if len(set(i)) == 3:
                ct = ct + 1
        return ct