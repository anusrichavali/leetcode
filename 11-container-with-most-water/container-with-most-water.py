class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, area)
            if(height[left] <= height[right]):
                left += 1
            else:
                right -= 1
        return maxArea