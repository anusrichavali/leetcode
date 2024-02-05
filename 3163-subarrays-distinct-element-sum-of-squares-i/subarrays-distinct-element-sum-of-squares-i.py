class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        for i in range(len(nums)):
            for j in range(0, len(nums) - i, 1):
                sub = nums[j: j + i + 1: 1]
                l.append(len(set(sub)) ** 2)
        return sum(l)
        