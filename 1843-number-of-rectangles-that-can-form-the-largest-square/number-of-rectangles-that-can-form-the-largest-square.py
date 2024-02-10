class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        l2 = []
        for i in rectangles:
            l2.append(min(i))

        return l2.count(max(l2))