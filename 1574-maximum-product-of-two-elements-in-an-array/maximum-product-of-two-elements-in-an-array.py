class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        nums.pop(nums.index(m))
        j = max(nums)
        return (m - 1) * (j - 1)