class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        b = []
        m = max(candies)
        for i in candies:
            if extraCandies + i >= m:
                b.append(True)
            else:
                b.append(False)
        return b
        