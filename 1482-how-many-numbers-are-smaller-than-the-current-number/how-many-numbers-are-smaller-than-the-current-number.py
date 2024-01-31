class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count = count + 1
            counts.append(count)
        return counts