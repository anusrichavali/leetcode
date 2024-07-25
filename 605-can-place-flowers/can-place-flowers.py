class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num = 0
        if len(flowerbed) == 1:
            return flowerbed == [0] or num == n
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i == 0:
                if flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    num+=1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    num+=1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    num+=1
        return num >= n

