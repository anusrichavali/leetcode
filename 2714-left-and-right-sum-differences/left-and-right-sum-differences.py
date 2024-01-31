class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                sums[i] = sums[i] + nums[j]
            for k in range(i + 1, len(nums)):
                sums[i] = sums[i] - nums[k]
            sums[i] = abs(sums[i])

        return sums
            

        