class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = -(heapq.heappop(stones))
            b = -(heapq.heappop(stones))
            if b > a:
                heapq.heappush(stones, a - b)
            elif b < a:
                heapq.heappush(stones, b - a)
        if stones:
            return -(heapq.heappop(stones))
        else:
            return 0
        