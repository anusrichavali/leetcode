class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for i in range(1, len(nums) + 1):
            if len(nums) % i == 0:
                s += nums[i - 1] * nums[i - 1]
        return s
        