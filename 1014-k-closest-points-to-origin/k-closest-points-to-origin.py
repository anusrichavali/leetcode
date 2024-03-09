class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for point in range(len(points)):
            x, y = points[point]
            distance = math.sqrt(x**2 + y**2)
            points[point] = (distance, x, y)
        heapq.heapify(points)
        result = []
        while len(result) < k:
            dist, x, y = heapq.heappop(points)
            result.append((x, y))
        return result