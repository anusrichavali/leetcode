class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        sum_water = 0
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                sum_water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                sum_water += maxR - height[r]
        return sum_water
        