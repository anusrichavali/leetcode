class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x = []
        for pt in points:
            x.append(pt[0])
        x.sort()
        diff = 0
        for i in range(len(x) - 1):
            if x[i + 1] - x[i] > diff:
                diff = x[i + 1] - x[i]
        
        return diff
        