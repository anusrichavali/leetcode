class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        s = 0
        for i in range(1, len(points)):
            x = abs(points[i][0] - points[i - 1][0])
            y = abs(points[i][1] - points[i - 1][1])
            s += max(x, y)
        return s
        