class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = m2 = 1
        for i in range(2):
            m1 *= nums.pop(nums.index(max(nums)))
            m2 *= nums.pop(nums.index(min(nums)))
        return m1 - m2