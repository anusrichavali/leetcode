class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        j = list(jewels)
        count = 0
        for i in stones:
            if i in j:
                count = count + 1
        return count