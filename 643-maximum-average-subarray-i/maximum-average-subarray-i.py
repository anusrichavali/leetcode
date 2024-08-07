class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = float('-inf')
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        max_sum = curr_sum
        for i in range(k, len(nums)):
            curr_sum -= nums[i - k]
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        return round(max_sum/float(k), 5)



        