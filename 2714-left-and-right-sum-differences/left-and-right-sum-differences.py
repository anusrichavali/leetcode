class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSums = [0] * len(nums)
        rightSums = [0] * len(nums)
        sums = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                leftSums[i] = leftSums[i] + nums[j]
            for k in range(i + 1, len(nums)):
                rightSums[i] = rightSums[i] + nums[k]

        for i in range(len(nums)):
            sums[i] = abs(leftSums[i] - rightSums[i])
        return sums
            

        