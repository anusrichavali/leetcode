class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        increment = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                increment += prev - nums[i] + 1
                nums[i] = nums[i] + (prev - nums[i] + 1)
            prev = nums[i]
        return increment

        