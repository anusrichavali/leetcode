class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        l = []
        while i < len(nums):
            for j in range(nums[i]):
                l.append(nums[i + 1])
            i = i + 2
        return l
        