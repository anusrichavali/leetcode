class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        res = [False] * len(candies)
        for i in range(len(candies)):
            if extraCandies + candies[i] >= max_candies:
                res[i] = True
        return res